-- HR ANALYTICS SQL PROJECT
-- Author: Ramit Sakhuja

SELECT 
    COUNT(*) AS Total_Employees
FROM
    employee_attrition;

-- 2. Attrition Count
SELECT 
    COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes';

-- 3. Attrition Rate
SELECT 
    ROUND(SUM(CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END) * 100.0 / COUNT(*),
            2) AS Attrition_Rate
FROM
    employee_attrition;

-- 4. Average Employee Age
SELECT 
    ROUND(AVG(Age), 2) AS Average_Age
FROM
    employee_attrition;

-- 5. Average Monthly Income
SELECT 
    ROUND(AVG(MonthlyIncome), 2) AS Average_Monthly_Income
FROM
    employee_attrition;

-- 6. Employee Distribution by Department
SELECT 
    Department, COUNT(*) AS Employee_Count
FROM
    employee_attrition
GROUP BY Department
ORDER BY Employee_Count DESC;

-- 7. Attrition by Department
SELECT 
    Department, COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY Department
ORDER BY Attrition_Count DESC;

-- 8. Average Salary by Department
SELECT 
    Department, ROUND(AVG(MonthlyIncome), 2) AS Avg_Salary
FROM
    employee_attrition
GROUP BY Department
ORDER BY Avg_Salary DESC;

-- 9. Employee Distribution by Gender
SELECT 
    Gender, COUNT(*) AS Employee_Count
FROM
    employee_attrition
GROUP BY Gender;

-- 10. Attrition by Gender
SELECT 
    Gender, COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY Gender
ORDER BY Attrition_Count DESC;

-- 11. Attrition by Marital Status
SELECT 
    MaritalStatus, COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY MaritalStatus
ORDER BY Attrition_Count DESC;

-- 12. Attrition by Education Field
SELECT 
    EducationField, COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY EducationField
ORDER BY Attrition_Count DESC;

-- 13. Attrition by Job Role
SELECT 
    JobRole, COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY JobRole
ORDER BY Attrition_Count DESC;

-- 14. Attrition by Overtime
SELECT 
    OverTime, COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY OverTime;

-- 15. Attrition by Job Satisfaction
SELECT 
    JobSatisfaction, COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;

-- 16. Attrition by Environment Satisfaction
SELECT 
    EnvironmentSatisfaction, COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY EnvironmentSatisfaction
ORDER BY EnvironmentSatisfaction;

-- 17. Attrition by Work Life Balance
SELECT 
    WorkLifeBalance, COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY WorkLifeBalance
ORDER BY WorkLifeBalance;

-- 18. Tenure Band Analysis
SELECT 
    CASE
        WHEN YearsAtCompany <= 2 THEN '0-2 Years'
        WHEN YearsAtCompany <= 5 THEN '3-5 Years'
        WHEN YearsAtCompany <= 10 THEN '6-10 Years'
        ELSE '11+ Years'
    END AS Tenure_Band,
    COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY Tenure_Band
ORDER BY Attrition_Count DESC;

-- 19. Salary Band Analysis
SELECT 
    CASE
        WHEN MonthlyIncome < 5000 THEN 'Low Income'
        WHEN MonthlyIncome < 10000 THEN 'Medium Income'
        ELSE 'High Income'
    END AS Salary_Band,
    COUNT(*) AS Attrition_Count
FROM
    employee_attrition
WHERE
    Attrition = 'Yes'
GROUP BY Salary_Band
ORDER BY Attrition_Count DESC;


-- 20. Top 5 Highest Paying Job Roles
SELECT 
    JobRole, ROUND(AVG(MonthlyIncome), 2) AS Avg_Salary
FROM
    employee_attrition
GROUP BY JobRole
ORDER BY Avg_Salary DESC
LIMIT 5;

-- 21. Department-wise Attrition Rate
SELECT 
    Department,
    COUNT(CASE
        WHEN Attrition = 'Yes' THEN 1
    END) AS Attrition_Count,
    COUNT(*) AS Total_Employees,
    ROUND(COUNT(CASE
                WHEN Attrition = 'Yes' THEN 1
            END) * 100.0 / COUNT(*),
            2) AS Attrition_Rate
FROM
    employee_attrition
GROUP BY Department
ORDER BY Attrition_Rate DESC;

-- 22. Rank Job Roles by Attrition
SELECT
	JobRole,
	COUNT(*) AS Attrition_Count,
	RANK() OVER(
		ORDER BY COUNT(*) DESC
	) AS Attrition_Rank
FROM 
	employee_attrition
WHERE 
	Attrition='Yes'
GROUP BY JobRole;
