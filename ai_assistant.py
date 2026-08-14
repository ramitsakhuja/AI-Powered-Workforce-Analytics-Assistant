import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"

SCHEMA = """
Table: employee_attrition
Columns:
  Age INTEGER, Attrition TEXT ('Yes'/'No'), BusinessTravel TEXT, DailyRate INTEGER,
  Department TEXT, DistanceFromHome INTEGER, Education INTEGER, EducationField TEXT,
  EmployeeCount INTEGER, EmployeeNumber INTEGER, EnvironmentSatisfaction INTEGER,
  Gender TEXT, HourlyRate INTEGER, JobInvolvement INTEGER, JobLevel INTEGER,
  JobRole TEXT, JobSatisfaction INTEGER, MaritalStatus TEXT, MonthlyIncome INTEGER,
  MonthlyRate INTEGER, NumCompaniesWorked INTEGER, Over18 TEXT, OverTime TEXT ('Yes'/'No'),
  PercentSalaryHike INTEGER, PerformanceRating INTEGER, RelationshipSatisfaction INTEGER,
  StandardHours INTEGER, StockOptionLevel INTEGER, TotalWorkingYears INTEGER,
  TrainingTimesLastYear INTEGER, WorkLifeBalance INTEGER, YearsAtCompany INTEGER,
  YearsInCurrentRole INTEGER, YearsSinceLastPromotion INTEGER, YearsWithCurrManager INTEGER
"""


def generate_sql(question, error_feedback=None):
    """
    Asks the LLM to translate a natural-language question into a single
    read-only SQLite SELECT query against the employee_attrition table.
    Returns the raw SQL string (no markdown fences, no commentary).
    """

    system_prompt = f"""
You are a SQL generator for a SQLite database with this schema:

{SCHEMA}

Rules:
- Output ONLY a single valid SQLite SELECT statement. No markdown, no
  backticks, no explanation, no semicolon-separated multiple statements.
- Never use INSERT, UPDATE, DELETE, DROP, ALTER, ATTACH, PRAGMA, or any
  statement other than SELECT.
- Use ROUND(..., 2) for percentages/averages where it makes results readable.
- If the question is ambiguous, make a reasonable assumption and answer it
  with a single SELECT rather than asking for clarification.
- Always add a LIMIT (50 by default) unless the question clearly wants a
  single aggregate value.
"""

    user_prompt = f"Question: {question}"
    if error_feedback:
        user_prompt += (
            f"\n\nYour previous query failed with this error:\n{error_feedback}\n"
            "Fix the query and return only the corrected SQL."
        )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
    )

    sql = response.choices[0].message.content.strip()

    # Strip accidental markdown fences if the model adds them anyway.
    if sql.startswith("```"):
        sql = sql.strip("`")
        sql = sql.replace("sql\n", "", 1).replace("sql", "", 1)

    return sql.strip().rstrip(";")


def explain_answer(question, sql_answer):
    """
    Converts SQL output into a professional business explanation.
    """

    prompt = f"""
You are an HR Analytics Assistant.

A SQL query has already calculated the correct answer.

Do NOT change the numbers.

Simply explain the answer in simple business language.

User Question:
{question}

SQL Result:
{sql_answer}

Rules:
- Keep the response under 80 words.
- Use professional HR/business language.
- Do not invent facts.
- Use only the SQL result provided.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content
