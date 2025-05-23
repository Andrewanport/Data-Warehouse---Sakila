# 📊 DW-Sakila - Data Warehouse Project

This project consists of building a **Data Warehouse (DW)** based on the [Sakila database](https://dev.mysql.com/doc/sakila/en/) using PostgreSQL. It was developed for academic purposes to demonstrate skills in data modeling, ETL processes, and dashboard creation using Metabase.

---
## 🔎 Metabase Visualization

![gif1](https://github.com/user-attachments/assets/e3c4dabe-ee3b-4d13-9123-eeac06102547)

![gif2](https://github.com/user-attachments/assets/d324089d-22ed-40ac-9d25-39ccc303f40f)

![gif3](https://github.com/user-attachments/assets/71b150df-7f13-4472-8052-19835bd98eb2)

---

## 🚀 Objective

To consolidate and analyze rental data from the Sakila database through a dimensional model, enabling the generation of strategic insights such as:

- Total revenue
- Revenue by store and film
- Monthly revenue
- Monthly sales
- Most profitable films
- Top 3 stores by revenue

---

## 🛠️ Technologies Used

- **PostgreSQL** - DW and source database
- **Python** with `Pandas` and `SQLAlchemy` - ETL implementation
- **Docker** - create, deploy, and manage the application in container
- **Metabase** - Dashboard and data visualization
- **DBeaver** - Database management
- **PyCharm** - Python development environment

---

## 📐 DW Modeling

The **Star Schema** was designed with the following tables:

### Dimensions:
- `dim_tempo` (Date)
- `dim_cliente` (Customer)
- `dim_funcionario` (Employee)
- `dim_filme` (Film)
- `dim_loja` (Store)

### Fact Table:
- `fato_pagamento` (Payments)

---

## 🔄 ETL (Extract, Transform, Load)

Python scripts were created for each dimension and fact table:

```
etl_dim_tempo.py
etl_dim_cliente.py
etl_dim_funcionario.py
etl_dim_filme.py
etl_dim_loja.py
etl_fato_pagamento.py
```

Each script:
- Connects to the source database
- Transforms the data as needed (e.g., formatting names, calculating fields)
- Loads the data into the `dw` schema

---

## 📊 Dashboards (Metabase)

The project includes a set of dashboards:

### 📌 Summary Dashboard
- Total Revenue
- Revenue by Store
- Revenue by Film
- Monthly Revenue
- Average Ticket per Sale
- Top 3 Stores by Revenue
- Most Profitable Films

### 🎬 Film Analysis *(coming soon)*
### 🧑‍🤝‍🧑 Customer/Employee Analysis *(coming soon)*

---

## 📁 Repository Structure

```
DW-Sakila/
├── etl_dim_cliente.py
├── etl_dim_funcionario.py
├── etl_dim_filme.py
├── etl_dim_loja.py
├── etl_dim_tempo.py
├── etl_fato_pagamento.py
├── README.md
```

---

## ▶️ How to Run Locally

1. Clone the repository
2. Set up PostgreSQL with the Sakila source database and create the `dw` schema
3. Open the project in PyCharm and create a virtual environment (Python 3.12 recommended)
4. Run each ETL script in the suggested order
5. Open Metabase and connect it to the PostgreSQL DW
6. Import or recreate the dashboards

---

## 📚 Notes

- All data was generated based on the Sakila structure. Additional fictional data was added to simulate real business scenarios.
- This project is educational and not intended for production use.

---

Made with 💡 by [Andrewanport]
