import sqlite3
import re
from ai_assistant import explain_answer

def run_query(query):
    conn = sqlite3.connect("hr_analytics.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def clean_question(question):
    question = question.lower()
    question = re.sub(r"[^\w\s]", "", question)
    return question

def get_answer(question):
    question = clean_question(question)
    words = question.split()
    greetings = {
        "hi",
        "hello",
        "hey",
        "good",
        "morning",
        "evening"
    }

    if greetings.intersection(words):

        return (
            "👋 Hello! I'm your AI Workforce Analytics Assistant.\n\n"
            "I can answer questions about:\n"
            "• Employee Attrition\n"
            "• Departments\n"
            "• Job Roles\n"
            "• Salary\n"
            "• Overtime\n"
            "• Tenure\n"
            "• Executive Summary"
        )

    if (
        "thanks" in words
        or ("thank" in words and "you" in words)
    ):

        return (
            "You're welcome! 😊\n\n"
            "Feel free to ask more questions about your HR dataset."
        )

    if (
        "employee" in question
        and (
            "total" in question
            or "count" in question
            or "number" in question
            or "workforce" in question
        )
    ):

        result = run_query("""
            SELECT COUNT(*)
            FROM employee_attrition
        """)

        return explain_answer(
            question,
            f"Total Employees: {result[0][0]}"
        )

    elif (
        "attrition" in question
        and (
            "count" in question
            or "left" in question
            or "exit" in question
            or "employees left" in question
        )
    ):

        result = run_query("""
            SELECT COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
        """)

        return explain_answer(
            question,
            f"Attrition Count: {result[0][0]}"
        )

    elif (
        "attrition" in question
        and "rate" in question
    ):

        result = run_query("""
            SELECT ROUND(
                SUM(
                    CASE
                        WHEN Attrition='Yes'
                        THEN 1
                        ELSE 0
                    END
                ) * 100.0 / COUNT(*),
            2)
            FROM employee_attrition
        """)

        return explain_answer(
            question,
            f"Attrition Rate: {result[0][0]}%"
        )
    
    elif "age" in question:

        result = run_query("""
            SELECT ROUND(
                AVG(Age),
            2)
            FROM employee_attrition
        """)

        return explain_answer(
            question,
            f"Average Employee Age: {result[0][0]} years"
        )

    elif (
        "salary" in question
        or "income" in question
        or "monthly" in question
    ):

        result = run_query("""
            SELECT ROUND(
                AVG(MonthlyIncome),
            2)
            FROM employee_attrition
        """)

        return explain_answer(
            question,
            f"Average Monthly Income: ${result[0][0]}"
        )

    elif (
        "department" in question
        and "attrition" in question
    ):

        result = run_query("""
            SELECT Department,
                   COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY Department
            ORDER BY COUNT(*) DESC
            LIMIT 1
        """)

        return explain_answer(
            question,
            f"{result[0][0]} has the highest attrition with {result[0][1]} employee exits."
        )

    elif (
        ("job" in question or "role" in question)
        and "attrition" in question
    ):

        result = run_query("""
            SELECT JobRole,
                   COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY JobRole
            ORDER BY COUNT(*) DESC
            LIMIT 1
        """)

        return explain_answer(
            question,
            f"{result[0][0]} has the highest attrition with {result[0][1]} employee exits."
        )

    elif "overtime" in question:

        result = run_query("""
            SELECT OverTime,
                   COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY OverTime
            ORDER BY COUNT(*) DESC
        """)

        summary = "\n".join(
            [
                f"{row[0]} : {row[1]} employees"
                for row in result
            ]
        )

        return explain_answer(
            question,
            summary
        )
    
    elif (
        "salary band" in question
        or "income band" in question
        or (
            "salary" in question
            and "band" in question
        )
    ):

        result = run_query("""
            SELECT
                CASE
                    WHEN MonthlyIncome < 5000
                        THEN 'Low Income'
                    WHEN MonthlyIncome < 10000
                        THEN 'Medium Income'
                    ELSE 'High Income'
                END AS Salary_Band,
                COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY Salary_Band
            ORDER BY COUNT(*) DESC
        """)

        summary = "\n".join(
            [
                f"{row[0]} : {row[1]} employees"
                for row in result
            ]
        )

        return explain_answer(
            question,
            summary
        )

    elif (
        "tenure" in question
        or "years" in question
        or "company" in question
    ):

        result = run_query("""
            SELECT
                CASE
                    WHEN YearsAtCompany <= 2
                        THEN '0-2 Years'
                    WHEN YearsAtCompany <= 5
                        THEN '3-5 Years'
                    WHEN YearsAtCompany <= 10
                        THEN '6-10 Years'
                    ELSE '11+ Years'
                END,
                COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY 1
            ORDER BY COUNT(*) DESC
        """)

        summary = "\n".join(
            [
                f"{row[0]} : {row[1]} employees"
                for row in result
            ]
        )

        return explain_answer(
            question,
            summary
        )

    elif (
        "summary" in question
        or "overview" in question
        or "dashboard" in question
        or "report" in question
    ):

        total = run_query("""
            SELECT COUNT(*)
            FROM employee_attrition
        """)[0][0]

        attrition = run_query("""
            SELECT COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
        """)[0][0]

        rate = run_query("""
            SELECT ROUND(
                SUM(
                    CASE
                        WHEN Attrition='Yes'
                        THEN 1
                        ELSE 0
                    END
                ) * 100.0 / COUNT(*),
            2)
            FROM employee_attrition
        """)[0][0]

        department = run_query("""
            SELECT Department
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY Department
            ORDER BY COUNT(*) DESC
            LIMIT 1
        """)[0][0]

        role = run_query("""
            SELECT JobRole
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY JobRole
            ORDER BY COUNT(*) DESC
            LIMIT 1
        """)[0][0]

        summary = f"""
Total Employees: {total}

Attrition Count: {attrition}

Attrition Rate: {rate}%

Highest Attrition Department: {department}

Highest Attrition Job Role: {role}
"""

        return explain_answer(
            question,
            summary
        )
    
    else:
        return """
    ❌ I couldn't understand that question.

    Here are some examples you can ask:

    👥 How many employees are there?

    📉 What is the attrition rate?

    🏢 Which department has the highest attrition?

    💼 Which job role has the highest attrition?

    💰 What is the average monthly income?

    📊 Show salary band analysis.

    📅 Show tenure analysis.

    ⏰ Does overtime affect attrition?

    📋 Give me an executive summary.
    """