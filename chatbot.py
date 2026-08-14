import re
import sqlite3

from ai_assistant import explain_answer, generate_sql

DB_PATH = "hr_analytics.db"
ALLOWED_TABLE = "employee_attrition"
MAX_SQL_RETRIES = 2

FORBIDDEN_KEYWORDS = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|ATTACH|DETACH|PRAGMA|REPLACE|"
    r"CREATE|TRUNCATE|VACUUM)\b",
    re.IGNORECASE,
)


def is_safe_select(sql: str) -> tuple[bool, str]:
    """
    Guardrail before executing anything the LLM writes. Returns
    (is_safe, reason_if_not).
    """
    if not sql:
        return False, "empty query"

    if ";" in sql.strip().rstrip(";"):
        return False, "multiple statements are not allowed"

    if not sql.strip().upper().startswith("SELECT"):
        return False, "only SELECT statements are allowed"

    if FORBIDDEN_KEYWORDS.search(sql):
        return False, "query contains a forbidden keyword"

    if ALLOWED_TABLE.lower() not in sql.lower():
        return False, f"query must reference the {ALLOWED_TABLE} table"

    return True, ""


def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)
    columns = [d[0] for d in cursor.description] if cursor.description else []
    rows = cursor.fetchall()
    conn.close()
    return columns, rows


def format_rows(columns, rows, max_rows=15):
    """Turns query results into a compact text table for the LLM + UI."""
    if not rows:
        return "No matching rows."

    lines = [" | ".join(columns)]
    for row in rows[:max_rows]:
        lines.append(" | ".join(str(v) for v in row))
    if len(rows) > max_rows:
        lines.append(f"... ({len(rows) - max_rows} more rows truncated)")
    return "\n".join(lines)


def clean_question(question):
    return question.lower().strip()


def handle_smalltalk(question):
    words = re.sub(r"[^\w\s]", "", question).split()
    greetings = {"hi", "hello", "hey", "good", "morning", "evening"}

    if greetings.intersection(words):
        return (
            "👋 Hello! I'm your AI Workforce Analytics Assistant.\n\n"
            "Ask me anything about the workforce data — attrition, "
            "departments, roles, salary, overtime, tenure, and more. "
            "I'll write and run the SQL myself."
        )

    if "thanks" in words or ("thank" in words and "you" in words):
        return "You're welcome! 😊 Feel free to ask more about the dataset."

    return None


def get_answer(raw_question, show_sql=False):
    """
    Full text-to-SQL flow:
    1. Handle greetings/thanks without hitting the LLM or DB.
    2. Ask the LLM to write a SQL query for the question.
    3. Validate the query (read-only, single statement, correct table).
    4. Run it, retrying with the error fed back to the LLM if it fails.
    5. Ask the LLM to explain the result in plain business language.

    Returns (answer_text, generated_sql) so the UI can optionally show
    the query that was actually run.
    """
    question = clean_question(raw_question)

    smalltalk = handle_smalltalk(question)
    if smalltalk:
        return smalltalk, None

    sql = generate_sql(raw_question)
    error_feedback = None

    for attempt in range(MAX_SQL_RETRIES + 1):
        safe, reason = is_safe_select(sql)
        if not safe:
            error_feedback = f"Rejected: {reason}"
        else:
            try:
                columns, rows = run_query(sql)
                result_text = format_rows(columns, rows)
                answer = explain_answer(raw_question, result_text)
                return answer, sql
            except sqlite3.Error as e:
                error_feedback = str(e)

        if attempt < MAX_SQL_RETRIES:
            sql = generate_sql(raw_question, error_feedback=error_feedback)

    return (
        "❌ I wasn't able to build a safe, working SQL query for that "
        "question. Try rephrasing it, or ask something like:\n\n"
        "• Which department has the highest attrition?\n"
        "• What is the average monthly income by job role?\n"
        "• How does overtime affect attrition?",
        sql,
    )
