# 💬 AI-Powered Workforce Analytics Assistant

> An end-to-end HR Analytics project that combines **SQL, Power BI, Python, SQLite, Streamlit, and Groq LLM** to transform workforce data into actionable business insights through an AI-powered conversational assistant.

---

## 📌 Project Overview

This project analyzes workforce data for **1,470 employees** to uncover employee attrition patterns, workforce demographics, compensation trends, and key retention drivers.

Beyond interactive dashboards, the project includes a **Conversational Workforce Analytics Assistant** that enables users to ask HR-related questions in natural language and receive concise, business-friendly insights powered by **Groq LLM**.

---

# 🚀 Project Features

### 📊 Interactive Power BI Dashboard

- Executive Workforce Overview
- Employee Attrition Analysis
- Workforce Demographics
- Salary & Compensation Insights
- Employee Retention Drivers
- Dynamic Filters & KPIs
- Interactive Visualizations

---

### 🤖 AI Workforce Analytics Assistant

Ask questions such as:

- How many employees are there?
- What is the attrition rate?
- Which department has the highest attrition?
- Which job role has the highest attrition?
- Does overtime affect attrition?
- Show salary band analysis.
- Show tenure analysis.
- Give me an executive summary.

The assistant:

- Retrieves answers directly from a SQLite database
- Executes SQL queries
- Uses Groq LLM to generate professional business explanations
- Never fabricates numerical results

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| Database | SQLite |
| Query Language | SQL |
| Data Visualization | Power BI |
| AI | Groq Llama 3.3 70B |
| Web App | Streamlit |
| Libraries | Pandas, Python-dotenv |

---

# 📂 Project Structure

```text
AI-Powered-Workforce-Analytics-Assistant
│
├── Data
│   └── employee_attrition.csv
│
├── SQL Analysis
│   └── HR Analytics SQL Queries.sql
│
├── PowerBI Dashboard
│   ├── HR Analytics Dashboard.pbix
│   └── HR Analytics Dashboard.pdf
│
├── Screenshots
│   ├── dashboard_page1.png
│   ├── dashboard_page2.png
│   ├── dashboard_page3.png
│   └── chatbot.png
│
├── app.py
├── chatbot.py
├── ai_assistant.py
├── database.py
├── hr_analytics.db
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# 📊 Dashboard Preview

## Executive Overview

![Dashboard 1](Screenshots/dashboard_page1.png)

---

## Attrition Analysis

![Dashboard 2](Screenshots/dashboard_page2.png)

---

## Retention Drivers

![Dashboard 3](Screenshots/dashboard_page3.png)

---

# 🤖 AI Assistant

![Chatbot](Screenshots/chatbot.png)

The conversational assistant converts natural language questions into SQL-powered workforce insights and explains the results using Groq LLM.

---

# 🗄 SQL Analysis

The project includes **22 business-focused SQL queries**, including:

- Total Employees
- Attrition Count
- Attrition Rate
- Average Employee Age
- Average Monthly Income
- Department-wise Employee Distribution
- Department-wise Attrition
- Salary Analysis
- Gender Analysis
- Marital Status Analysis
- Education Field Analysis
- Job Role Analysis
- Overtime Analysis
- Job Satisfaction Analysis
- Environment Satisfaction
- Work-Life Balance
- Tenure Analysis
- Salary Band Analysis
- Highest Paying Job Roles
- Department-wise Attrition Rate
- Window Functions (Ranking)

---

# 🔄 AI Workflow

```text
User Question
      │
      ▼
Streamlit Interface
      │
      ▼
Python Chatbot
      │
      ▼
SQLite Database
      │
      ▼
SQL Query Execution
      │
      ▼
Query Result
      │
      ▼
Groq LLM
      │
      ▼
Business-Friendly Explanation
```

---

# 📈 Key Business Insights

- Workforce consists of **1,470 employees**
- Overall attrition rate is **16.12%**
- Research & Development has the highest employee attrition
- Laboratory Technicians experience the highest employee exits
- Employees with **0–2 years** of tenure are more likely to leave
- Lower salary bands show higher employee attrition
- Overtime is associated with increased employee exits

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/ramitsakhuja/AI-Powered-Workforce-Analytics-Assistant.git
```

Move into the project

```bash
cd AI-Powered-Workforce-Analytics-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=your_api_key_here
```

Create the SQLite database

```bash
python database.py
```

Run the application

```bash
streamlit run app.py
```

---

# 💡 Skills Demonstrated

- SQL
- SQLite
- Python
- Power BI
- Data Analysis
- Business Intelligence
- Streamlit
- Large Language Models (LLMs)
- Prompt Engineering
- API Integration
- Dashboard Design
- Data Storytelling

---

# 👨‍💻 Author

## Ramit Sakhuja

**B.Tech – Artificial Intelligence & Machine Learning**

Aspiring Data Analyst | AI Enthusiast

**LinkedIn:** https://www.linkedin.com/in/ramitsakhuja

**GitHub:** https://github.com/ramitsakhuja
