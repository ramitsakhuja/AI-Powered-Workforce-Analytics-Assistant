import sqlite3
from ai_assistant import explain_answer


def run_query(query):
    conn = sqlite3.connect("hr_analytics.db")
    cursor = conn.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    conn.close()

    return result


def get_answer(question):

    question = question.lower()

    if any(word in question for word in [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good evening"
    ]):
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

    elif any(word in question for word in [
    "thanks",
    "thank you",
    "great",
    "awesome"
]):
        return "You're welcome! Let me know if you'd like more insights from the HR dataset."

    if any(keyword in question for keyword in [
        "total employees",
        "how many employees",
        "employee count",
        "number of employees",
        "workforce size",
        "total workforce"
    ]):

        result = run_query("""
            SELECT COUNT(*)
            FROM employee_attrition
        """)

        return explain_answer(
            question,
            f"Total Employees: {result[0][0]}"
        )

    elif any(keyword in question for keyword in [
        "attrition count",
        "employees left",
        "employee exits",
        "how many left",
        "left company",
        "total attrition"
    ]):

        result = run_query("""
            SELECT COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
        """)

        return explain_answer(
            question,
            f"Attrition Count: {result[0][0]}"
        )

    elif any(keyword in question for keyword in [
        "attrition rate",
        "employee attrition rate",
        "what is the attrition rate"
    ]):

        result = run_query("""
            SELECT ROUND(
                SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0
                / COUNT(*),2)
            FROM employee_attrition
        """)

        return explain_answer(
            question,
            f"Attrition Rate: {result[0][0]}%"
        )

    elif any(keyword in question for keyword in [
        "average age",
        "mean age",
        "employee age"
    ]):

        result = run_query("""
            SELECT ROUND(AVG(Age),2)
            FROM employee_attrition
        """)

        return explain_answer(
            question,
            f"Average Employee Age: {result[0][0]} years"
        )

    elif any(keyword in question for keyword in [
        "average salary",
        "average income",
        "monthly income",
        "average monthly income"
    ]):

        result = run_query("""
            SELECT ROUND(AVG(MonthlyIncome),2)
            FROM employee_attrition
        """)

        return explain_answer(
            question,
            f"Average Monthly Income: ${result[0][0]}"
        )

    elif any(keyword in question for keyword in [
        "highest attrition department",
        "which department has highest attrition",
        "department attrition",
        "highest department"
    ]):

        result = run_query("""
            SELECT Department, COUNT(*)
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

    elif any(keyword in question for keyword in [
        "highest attrition job role",
        "highest attrition role",
        "job role attrition",
        "which job role has highest attrition"
    ]):

        result = run_query("""
            SELECT JobRole, COUNT(*)
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

    elif any(keyword in question for keyword in [
        "overtime",
        "does overtime affect attrition",
        "overtime attrition"
    ]):

        result = run_query("""
            SELECT OverTime, COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY OverTime
            ORDER BY COUNT(*) DESC
        """)

        summary = "\n".join(
            [f"{row[0]} : {row[1]} employees" for row in result]
        )

        return explain_answer(question, summary)

    elif any(keyword in question for keyword in [
        "salary band",
        "income band",
        "salary analysis"
    ]):

        result = run_query("""
            SELECT
            CASE
                WHEN MonthlyIncome < 5000 THEN 'Low Income'
                WHEN MonthlyIncome < 10000 THEN 'Medium Income'
                ELSE 'High Income'
            END AS Salary_Band,
            COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY Salary_Band
            ORDER BY COUNT(*) DESC
        """)

        summary = "\n".join(
            [f"{row[0]} : {row[1]} employees" for row in result]
        )

        return explain_answer(question, summary)

    elif any(keyword in question for keyword in [
        "tenure",
        "years at company",
        "tenure analysis"
    ]):

        result = run_query("""
            SELECT
            CASE
                WHEN YearsAtCompany <=2 THEN '0-2 Years'
                WHEN YearsAtCompany <=5 THEN '3-5 Years'
                WHEN YearsAtCompany <=10 THEN '6-10 Years'
                ELSE '11+ Years'
            END,
            COUNT(*)
            FROM employee_attrition
            WHERE Attrition='Yes'
            GROUP BY 1
            ORDER BY COUNT(*) DESC
        """)

        summary = "\n".join(
            [f"{row[0]} : {row[1]} employees" for row in result]
        )

        return explain_answer(question, summary)

    elif any(keyword in question for keyword in [
        "summary",
        "executive summary",
        "overview",
        "dashboard summary"
    ]):

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
                SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0
                /COUNT(*),2)
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
        
        return explain_answer(question, summary)

    else:
        return (
            "I'm your HR Analytics Assistant. I can answer questions about:\n\n"
            "• Total Employees\n"
            "• Attrition Count\n"
            "• Attrition Rate\n"
            "• Average Employee Age\n"
            "• Average Monthly Income\n"
            "• Highest Attrition Department\n"
            "• Highest Attrition Job Role\n"
            "• Overtime Analysis\n"
            "• Salary Band Analysis\n"
            "• Tenure Analysis\n"
            "• Executive Summary"
        )