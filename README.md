# ✈️ Flight Analytics System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-blue?style=for-the-badge&logo=postgresql)
![Analytics](https://img.shields.io/badge/Data-Analytics-green?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Visualization-Plotly-purple?style=for-the-badge&logo=plotly)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

</p>

---

# 🌐 Live Application

🚀 **Streamlit Deployment:**  
https://flight-analytics-system-1135.streamlit.app/

---

# 📌 Project Overview

The **Flight Analytics System** is a cloud-based SQL analytics dashboard built using:

- Streamlit
- PostgreSQL (Supabase)
- Plotly
- Python

The application enables users to explore flight routes, traffic patterns, and airline distributions using real-time PostgreSQL queries through an interactive analytics dashboard.

This project demonstrates an end-to-end analytics workflow:

```text
CSV Dataset
      ↓
Supabase PostgreSQL
      ↓
Python Query Layer
      ↓
Analytics Processing
      ↓
Interactive Streamlit Dashboard
```

---

# 🎯 Core Objectives

The project was designed to demonstrate:

- SQL query engineering
- Cloud database integration
- Backend abstraction layer design
- Real-world analytics workflows
- Interactive dashboard development
- Production-style deployment architecture

---

# 🏗️ System Architecture

```text
Streamlit UI (app.py)
        ↓
Database Query Layer (database.py)
        ↓
Supabase PostgreSQL Database
```

---

# ⚙️ Architecture Breakdown

## 🖥️ Streamlit UI Layer

Responsible for:

- User interaction
- Dashboard rendering
- Route selection workflow
- Plotly visualizations
- Analytics presentation

---

## 🗄️ Database Query Layer

Implemented inside:

```text
database.py
```

Responsibilities:

- PostgreSQL connection management
- Query abstraction
- Parameterized SQL execution
- Analytics query handling

---

## ☁️ Cloud Database Layer

Hosted on:

- Supabase PostgreSQL

Stores:

- flight routes
- airline data
- airport traffic information
- daily flight statistics

---

# ✨ Main Features

## ✈️ Flight Search System

Users can:

- Select source city
- Select destination city
- Search available flight routes

### Smart Route Filtering

The destination dropdown dynamically updates based on the selected source city.

This prevents invalid route combinations and improves query efficiency.

---

## 📊 Airline Distribution Analytics

Interactive Plotly pie chart showing:

- airline frequency
- market distribution
- traffic contribution

---

## 🏙️ Busy Airports Analysis

Visualizes airport traffic using combined:

- source traffic
- destination traffic

Helps identify:

- high-traffic hubs
- major airport activity patterns

---

## 📅 Daily Flight Trends

Line chart visualization showing:

- daily flight frequency
- temporal traffic patterns
- trend distribution

---

# 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| Database | Supabase PostgreSQL |
| DB Connector | psycopg2 |
| Data Processing | Pandas |
| Visualization | Plotly |
| Deployment | Streamlit Cloud |

---

# 📂 Project Structure

```text
flight-analytics-system/
│
├── app.py
├── database.py
├── flights.csv
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🗄️ Database Schema

The PostgreSQL table:

```text
flights
```

contains:

```text
Airline
Date_of_Journey
Source
Destination
Route
Dep_Time
Duration
Total_Stops
Price
```

The application supports PostgreSQL quoted column handling for compatibility with CSV-imported schemas.

---

# 🔐 Secure Database Configuration

Database credentials are securely managed using:

- Streamlit Secrets
- SSL-enabled PostgreSQL connections

Example configuration:

```toml
DB_HOST = "your-supabase-db-host"
DB_USER = "postgres"
DB_PASSWORD = "your-password"
DB_NAME = "postgres"
DB_PORT = "6543"
```

---

# ⚙️ Local Setup & Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/flight-analytics-system.git
cd flight-analytics-system
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Streamlit Secrets

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
DB_HOST = "your-supabase-db-host"
DB_USER = "postgres"
DB_PASSWORD = "your-password"
DB_NAME = "postgres"
DB_PORT = "6543"
```

---

## 5️⃣ Run Application

```bash
streamlit run app.py
```

---

# 📊 Engineering Highlights

- Cloud PostgreSQL integration
- Supabase deployment architecture
- Secure secrets-based configuration
- Parameterized SQL query execution
- PostgreSQL transaction handling
- SSL-enabled database connectivity
- Backend query abstraction layer
- Interactive Plotly analytics dashboards
- Dynamic route-aware filtering system
- Production-style deployment debugging

---

# 📈 Analytics Modules

## ✈️ Flight Search

- Source-aware route filtering
- Dynamic destination selection
- Parameterized SQL querying

---

## 📊 Airline Analytics

- Airline distribution visualization
- Frequency-based aggregation queries

---

## 🏙️ Airport Traffic Insights

- Combined source/destination analytics
- High-traffic airport discovery

---

## 📅 Daily Trend Analysis

- Daily flight aggregation
- Time-series visualization

---

# 🌐 Deployment

The application is deployed using:

- Streamlit Cloud
- Supabase PostgreSQL

Deployment requirements:

- Active Supabase database
- SSL-enabled PostgreSQL connections
- Streamlit secrets configuration
- Populated `flights` table

---

# 🔐 Security Practices

Implemented security measures:

- Environment-based secrets management
- SSL-required PostgreSQL connections
- Parameterized SQL queries
- No hardcoded credentials
- Cloud database isolation

---

# ⚠️ Current Limitations

Current constraints include:

- No query caching
- No authentication system
- No API serving layer
- No pagination for large datasets
- No asynchronous query handling
- Tight coupling between UI and query layer

---

# 🚀 Future Improvements

Planned upgrades include:

- FastAPI backend layer
- Query caching with `st.cache_data`
- Docker containerization
- AWS RDS migration
- Analytics REST APIs
- Authentication system
- Query optimization & indexing
- CI/CD deployment pipeline
- Service-oriented backend architecture

---

# 🎯 What This Project Demonstrates

This project demonstrates practical understanding of:

- Cloud SQL database integration
- Backend query abstraction
- PostgreSQL analytics workflows
- Interactive dashboard deployment
- Production debugging workflows
- Secure credential management
- Data analytics system design
- End-to-end deployment architecture

---

# 📌 Strategic Engineering Value

This project demonstrates significantly more engineering depth than a local notebook analytics workflow because it includes:

- Cloud database deployment
- Real backend integration
- SQL analytics architecture
- Streamlit production deployment
- Configuration management
- Secure secrets handling
- Database transaction debugging

---

# 📸 Recommended Screenshot Section

Add application screenshots here for stronger recruiter impact:

```markdown
![Flight Search](your-image-link)
![Analytics Dashboard](your-image-link)
![Busy Airports](your-image-link)
```

---

# 👨‍💻 Author

## Rudra Tyagi

### Focus Areas

- ML Systems
- MLOps
- AI Infrastructure
- Backend Analytics Systems
- Applied Machine Learning

---

# ⭐ Recruiter Notes

This repository demonstrates:

- Real cloud database integration
- SQL query engineering
- Backend abstraction architecture
- Interactive analytics deployment
- Production debugging capability
- Full-stack analytics workflows
- Secure deployment configuration

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
