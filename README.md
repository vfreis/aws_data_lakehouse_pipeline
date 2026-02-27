<h1 align="center">
🚀 AWS Data Lakehouse Pipeline
</h1>

<h3 align="center">
Scalable Data Engineering Architecture using AWS, Spark & Airflow
</h3>

<p align="center">
<img src="https://img.shields.io/badge/AWS-Data%20Engineering-orange?style=for-the-badge&logo=amazonaws"/>
<img src="https://img.shields.io/badge/Python-ETL-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Apache%20Spark-Processing-red?style=for-the-badge&logo=apachespark"/>
<img src="https://img.shields.io/badge/Airflow-Orchestration-green?style=for-the-badge&logo=apacheairflow"/>
<img src="https://img.shields.io/badge/Data%20Lakehouse-Bronze%20%7C%20Silver-purple?style=for-the-badge"/>
</p>

---

## 📌 Overview

This project implements a **production-inspired AWS Data Lakehouse architecture**, designed to ingest, validate, transform and curate data using scalable distributed processing.

The pipeline follows modern **Data Engineering best practices**, separating data into logical layers:

✅ Bronze — Raw ingestion  
✅ Silver — Cleaned & validated datasets  

Built to simulate real-world enterprise data platforms.

---

## 🧱 Architecture


External API / Source
↓
Data Ingestion
↓
S3 Bronze
↓
Data Quality Checks
↓
Spark Transformation
↓
S3 Silver
↓
Analytics / BI / AI


---

## ⚙️ Tech Stack

| Layer | Technology |
|------|------------|
| Orchestration | Apache Airflow |
| Processing | Apache Spark |
| Cloud | AWS S3 + EMR |
| Language | Python |
| Data Validation | Custom Quality Framework |
| Architecture | Data Lakehouse |
| Processing Type | Batch / Incremental |

---

## 🔄 Pipeline Workflow

### 1️⃣ Data Ingestion (Bronze Layer)

- Extracts data from external APIs
- Stores raw immutable datasets
- Partitioned storage strategy
- Incremental ingestion supported

📂 `ingestion/api_ingestion.py`

---

### 2️⃣ Data Quality Validation

Ensures reliability before transformation:

- Schema validation
- Null checks
- Data consistency rules
- Logging & monitoring

📂 `utils/data_quality.py`

---

### 3️⃣ Transformation (Silver Layer)

Using Apache Spark:

- Data cleansing
- Standardization
- Business-ready structure
- Optimized parquet storage

📂 `spark_jobs/silver_transformation.py`

---

### 4️⃣ Orchestration

Airflow DAG manages:

- Execution order
- Dependency control
- Retry strategy
- Pipeline observability

📂 `dags/bronze_to_silver_pipeline.py`

---

## 📂 Project Structure


aws_data_lakehouse_pipeline/
│
├── dags/
├── ingestion/
├── spark_jobs/
├── utils/
├── configs/
├── architecture/
├── requirements.txt
└── README.md


---

## ✅ Engineering Features

✔ Incremental Processing  
✔ Modular Architecture  
✔ Data Quality Layer  
✔ Logging System  
✔ EMR Job Submission  
✔ Pipeline Orchestration  
✔ Scalable Cloud Design  

---

## 📈 Use Cases

- Enterprise Data Platforms
- Analytics Engineering
- Machine Learning datasets
- AI-ready data pipelines
- Cloud migration scenarios

---

## 🧠 Engineering Concepts Applied

- Data Lakehouse Architecture
- Distributed Processing
- Idempotent Pipelines
- Data Governance Principles
- Separation of Concerns
- Production-like Orchestration

---

## 🚀 Future Improvements

- Gold Layer (Business Aggregations)
- Streaming ingestion
- CI/CD Pipeline
- Infrastructure as Code (Terraform)
- Monitoring with CloudWatch

---

## 👨‍💻 Author

**Vinicios Falqueiro Reis**

Data Engineer focused on building scalable cloud data platforms.

🔗 LinkedIn  
https://www.linkedin.com/in/vfalqueiroreis/

🔗 GitHub  
https://github.com/vfreis
