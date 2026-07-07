# 💬 AI-Powered Workforce Analytics Assistant

An end-to-end HR Analytics project that combines **SQL, Power BI, Python, SQLite, Streamlit, and Groq LLM** to analyze employee attrition and provide AI-powered workforce insights through a conversational assistant.

---

## 📌 Project Overview

This project analyzes HR data for **1,470 employees** to identify workforce trends, employee attrition patterns, salary insights, tenure distribution, and key retention drivers.

In addition to interactive Power BI dashboards, the project includes an **AI-powered conversational assistant** that allows users to ask HR-related questions in natural language and receive business-friendly responses generated using Groq LLM.

---

## 🚀 Features

### 📊 Interactive Power BI Dashboard
- Executive Workforce Overview
- Employee Attrition Analysis
- Employee Retention Drivers
- Dynamic Filters & KPIs
- Business Insights Section

### 🤖 AI Workforce Analytics Assistant
Ask questions such as:

- How many employees are there?
- What is the attrition rate?
- Which department has the highest attrition?
- Which job role has the highest attrition?
- What is the average employee age?
- Give me an executive summary.
- Does overtime affect attrition?
- Show salary band analysis.
- Show tenure analysis.

---

## 🛠 Tech Stack

- **SQL (MySQL)** – Data Analysis
- **Power BI** – Dashboard Development
- **Python**
- **SQLite**
- **Streamlit**
- **Groq API (Llama 3.3 70B)**
- **Pandas**
- **Python Dotenv**

---


## 📊 Dashboard Highlights

### Executive Overview
- Total Employees
- Attrition Count
- Attrition Rate
- Average Age
- Average Monthly Income

### Attrition Analysis
- Department-wise Attrition
- Job Role Analysis
- Education Field Analysis
- Marital Status Analysis
- Tenure Analysis

### Employee Retention Drivers
- Salary Band Analysis
- Overtime Analysis
- Work-Life Balance
- Environment Satisfaction
- Job Satisfaction

---

## 🗄 SQL Analysis

The project includes **22 business-focused SQL queries** covering:

- Employee Count
- Attrition Count
- Attrition Rate
- Average Age
- Average Monthly Income
- Department Analysis
- Gender Analysis
- Job Role Analysis
- Education Field Analysis
- Marital Status Analysis
- Salary Band Analysis
- Tenure Analysis
- Department-wise Attrition Rate
- Highest Paying Job Roles
- Window Functions (Ranking)

---

## 🤖 AI Assistant Workflow

```
User Question
      │
      ▼
Streamlit Chat Interface
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
Natural Language Business Explanation
```

The chatbot retrieves data directly from the SQLite database using SQL queries and uses Groq LLM to convert the query results into concise, professional business insights.

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Powered-Workforce-Analytics-Assistant.git
```

Navigate to the project folder

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

## 📈 Key Business Insights

- Workforce consists of **1,470 employees**.
- Overall employee attrition rate is **16.12%**.
- Research & Development records the highest employee attrition.
- Laboratory Technicians show the highest employee turnover.
- Employees with **0–2 years** of tenure leave most frequently.
- Low-income employees experience the highest attrition.
- Overtime is associated with increased employee exits.

---

## 🎯 Skills Demonstrated

- SQL
- Data Analysis
- Business Intelligence
- Power BI
- Python
- SQLite
- Streamlit
- Large Language Models (LLMs)
- Prompt Engineering
- API Integration
- Dashboard Design
- Data Storytelling

---

## 👨‍💻 Author

**Ramit Sakhuja**

B.Tech (Artificial Intelligence & Machine Learning)

Aspiring Data Analyst | AI Enthusiast
