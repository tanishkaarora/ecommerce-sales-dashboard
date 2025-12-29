# 📊 E-Commerce Sales Dashboard

An end-to-end **E-Commerce Sales Analysis Dashboard** built using **FastAPI, SQLAlchemy, and Dash**.  
This project demonstrates how backend APIs, databases, and interactive dashboards work together to provide real-time business insights.

---

## 🚀 Project Overview

This project collects e-commerce sales data through a REST API, stores it in a database, and visualizes key business metrics using an interactive dashboard.  
It is designed to simulate a real-world analytics system used by businesses to monitor sales performance.

---

## 🧱 System Architecture (High Level)

- **FastAPI** – Handles sales data through REST APIs  
- **SQLAlchemy** – Manages database models and storage  
- **SQLite** – Stores sales records  
- **Dash & Plotly** – Visualizes data in an interactive dashboard  

---

## 📁 Project Structure

ecommerce-sales-dashboard/
│
├── main.py # FastAPI backend entry point
├── database.py # Database connection and setup
├── models.py # Database table definitions
├── schemas.py # Data validation schemas
├── add_data.py # Script to insert sample data
├── dashboard/
│ └── dashboard.py # Interactive dashboard application
└── README.md # Project documentation

---

## ⚙️ Features Implemented

### 🔹 Backend API
- REST API built using FastAPI
- Accepts sales data and stores it in the database
- Provides endpoints for data access

### 🔹 Database Management
- Sales data stored using SQLAlchemy ORM
- Structured schema with category, price, and quantity fields
- Automatic table creation on startup

### 🔹 Interactive Dashboard
- Real-time data visualization
- Business-oriented charts for decision making
- Clean and responsive interface

---

## 📊 Dashboard Insights

### 📌 Sales by Category
Shows how sales are distributed across different product categories, helping identify top-performing categories.

### 📌 Revenue Distribution
Displays how total revenue is generated from different categories based on price and quantity sold.

### 📌 Quantity Sold Analysis
Highlights the total number of units sold, useful for understanding demand trends.

### 📌 Interactive Visualizations
All charts are interactive, allowing users to explore data dynamically.

---

## ▶️ How to Run the Project

### 1️⃣ Start the Backend API
```bash
python main.py
```
API documentation will be available at:

http://127.0.0.1:8000/docs
2️⃣ Insert Sample Data
python add_data.py
3️⃣ Run the Dashboard
python dashboard/dashboard.py
Open in browser:

http://127.0.0.1:8050

🎯 Learning Outcomes

FastAPI REST API development

Database modeling using SQLAlchemy

Backend and dashboard integration

Data analysis and visualization

Real-world project structuring

Git & GitHub workflow

🧠 Use Case

This dashboard can be used by:

Business analysts

Sales managers

Students learning full-stack analytics

Academic project demonstrations

📌 Conclusion

This project demonstrates a complete data flow from API → Database → Dashboard, showcasing how backend systems power real-time business analytics in production-level applications.
