# E-Commerce Sales Dashboard 📊

An end-to-end **E-Commerce Sales Dashboard** built using **FastAPI**, **SQLAlchemy**, and **Dash**.  
This project demonstrates backend API development, database integration, and interactive data visualization.

---

## 🚀 Project Description

This project allows managing and visualizing e-commerce sales data through:
- A REST API for sales records
- A database for persistent storage
- An interactive dashboard for analytics

It is suitable for **academic submission, viva explanation, and portfolio projects**.

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- SQLAlchemy  
- SQLite  
- Dash & Plotly  
- Uvicorn

- 📂 Project Structure 

---ecom dashboard/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── add_data.py
├── dashboard/
│ └── dashboard.py
├── README.md
└── pycache/


---

## ⚙️ Features

- Create and fetch sales data via API  
- Store sales records in SQLite  
- Auto-create database tables  
- Interactive sales dashboard  
- Modular and clean code structure  

---

## ▶️ How to Run

### Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy dash plotly
uvicorn main:app --reload
API Docs:

http://127.0.0.1:8000/docs
Insert Sample Data
python add_data.py
Run Dashboard
python dashboard/dashboard.py
http://127.0.0.1:8050
##Dashboard Insights

Sales by category

Revenue distribution

Quantity sold analysis

Interactive visualizations

🎯 Learning Outcomes

FastAPI REST API development

Database modeling with SQLAlchemy

Backend–dashboard integration

Real-world project structuring

Git & GitHub workflow

👩‍💻 Author

Tanishka Arora
GitHub: https://github.com/tanishkaarora



