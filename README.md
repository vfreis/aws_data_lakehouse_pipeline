<h1 align="center">AWS Data Lakehouse Pipeline</h1>

<p align="center">
  Production-inspired data engineering architecture using AWS, PySpark, Apache Airflow, and layered lakehouse design.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=FF9900" alt="AWS" />
  <img src="https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white" alt="PySpark" />
  <img src="https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white" alt="Apache Airflow" />
  <img src="https://img.shields.io/badge/Amazon_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white" alt="Amazon S3" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-Bronze_%E2%86%92_Silver-0EA5E9?style=flat-square" alt="Bronze to Silver architecture" />
  <img src="https://img.shields.io/badge/Processing-Batch_%26_Incremental-334155?style=flat-square" alt="Batch and incremental processing" />
  <img src="https://img.shields.io/badge/Status-Portfolio_Project-16A34A?style=flat-square" alt="Portfolio project" />
</p>

---

## Overview

This repository implements a **production-inspired AWS data lakehouse pipeline** that moves data from external sources into raw and curated storage layers.

The project demonstrates how ingestion, validation, distributed transformation, and orchestration can be separated into maintainable components while preserving traceability between raw and processed datasets.

> This is a portfolio architecture designed to demonstrate engineering patterns. It is not presented as a deployed production service.

---

## Architecture

```text
External APIs / Sources
          │
          ▼
Python ingestion
          │
          ▼
Amazon S3 — Bronze
Immutable raw datasets
          │
          ▼
Data-quality validation
          │
          ▼
PySpark processing on Amazon EMR
          │
          ▼
Amazon S3 — Silver
Validated and curated Parquet datasets
          │
          ▼
Analytics · BI · AI workloads
```

### Layer responsibilities

| Layer | Responsibility |
|---|---|
| **Ingestion** | Extract data from external sources and persist raw records. |
| **Bronze** | Preserve immutable source data for replay and traceability. |
| **Quality** | Validate schema, nullability, consistency, and expected conditions. |
| **Processing** | Clean, standardize, and transform data using PySpark. |
| **Silver** | Store validated and curated datasets in Parquet format. |
| **Orchestration** | Manage dependencies, retries, execution order, and scheduling with Airflow. |

---

## Engineering Capabilities Demonstrated

- Modular ingestion, transformation, and validation components.
- Bronze and Silver lakehouse separation.
- Batch and incremental processing patterns.
- Distributed transformation with Apache Spark and PySpark.
- Apache Airflow orchestration with dependency and retry control.
- Data-quality checks before curated-layer delivery.
- Structured logging and production-oriented separation of concerns.
- Optimized Parquet output for downstream analytics workloads.
- EMR-oriented job submission and scalable cloud processing design.

---

## Technology Stack

| Area | Technologies |
|---|---|
| Cloud storage | Amazon S3 |
| Distributed processing | Apache Spark, PySpark, Amazon EMR |
| Orchestration | Apache Airflow |
| Language | Python |
| Data format | Parquet |
| Validation | Python-based data-quality rules |
| Architecture | Data lakehouse, Bronze and Silver layers |
| Processing modes | Batch and incremental |

---

## Pipeline Workflow

### 1. Bronze ingestion

The ingestion component extracts data from external APIs and writes raw, immutable datasets to the Bronze layer.

**Source:** [`ingestion/api_ingestion.py`](./ingestion/api_ingestion.py)

Key concepts:

- source-oriented ingestion;
- partitioned raw storage;
- replayable datasets;
- incremental ingestion support.

### 2. Data-quality validation

Validation runs before curated delivery to identify structural and content issues.

**Source:** [`utils/data_quality.py`](./utils/data_quality.py)

Checks represented in the project include:

- schema expectations;
- null checks;
- consistency rules;
- validation logging.

### 3. Silver transformation

PySpark transforms Bronze data into cleaned, standardized, business-ready datasets stored as Parquet.

**Source:** [`spark_jobs/silver_transformation.py`](./spark_jobs/silver_transformation.py)

### 4. Airflow orchestration

The DAG coordinates ingestion, validation, transformation, dependencies, and retries.

**Source:** [`dags/bronze_to_silver_pipeline.py`](./dags/bronze_to_silver_pipeline.py)

---

## Repository Structure

```text
aws_data_lakehouse_pipeline/
├── architecture/        # Architecture documentation and supporting assets
├── configs/             # Pipeline configuration
├── dags/                # Apache Airflow DAGs
├── ingestion/           # External-source ingestion
├── spark_jobs/          # PySpark transformation jobs
├── utils/               # Data-quality and shared utilities
├── requirements.txt     # Python dependencies
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.x
- An AWS account with access to S3 and EMR
- Apache Airflow environment
- AWS credentials configured outside the repository

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Review the files under `configs/` and provide environment-specific AWS settings before executing the pipeline components.

> Do not commit AWS credentials, access keys, secrets, or environment-specific tokens to the repository.

---

## Design Decisions

### Why Bronze and Silver?

The separation preserves source fidelity while allowing downstream consumers to use cleaned and standardized data without modifying raw records.

### Why Parquet?

Parquet provides a columnar storage format suited to analytical workloads and distributed processing.

### Why Airflow?

Airflow makes task dependencies, retries, scheduling, and pipeline state explicit instead of hiding orchestration inside individual scripts.

---

## Roadmap

- Gold layer for business aggregates.
- Automated tests for transformations and validation rules.
- Infrastructure as Code with Terraform.
- CI/CD validation for Python and DAG changes.
- CloudWatch-based monitoring and alerting.
- Additional source connectors.
- Streaming ingestion as a separate architecture path.

---

## Author

**Vinicios Falqueiro Reis** — Data Engineer focused on reliable cloud data platforms and scalable pipelines.

[LinkedIn](https://www.linkedin.com/in/vfalqueiroreis/) · [GitHub](https://github.com/vfreis)

---

## Technical QA note (2026-11-05)

**Scope:** This is a portfolio demonstration, not a verified production deployment.
The Silver script reads JSON-array source snapshots with `multiLine=true`,
validates the required fields, transforms data in Spark without collecting to
Pandas, and writes a **snapshot** Parquet output via `overwrite`.

**Not yet implemented:** transactional CDC, watermark advancement, Delta
`MERGE`/upsert, recoverable Silver-to-Gold incremental processing, and
end-to-end AWS/EMR integration tests. These remain engineering roadmap items.

**Orchestration caveat:** The current DAG uses Airflow `BashOperator` with
`spark-submit` on the task execution environment. The separate EMR steps
helper is not wired into the DAG, so this repository must not be presented as
proving an end-to-end EMR-submitted workflow.

**Quick contract tests:** Install pytest and run `python -m pytest tests -q`.
These tests mock the Spark interface and catch wiring regressions; they do
**not** prove execution on a real Spark/EMR cluster. The source API produces a
JSON array, not JSON Lines. Use the matching reader option.

**Next:** add local Spark integration tests with fixtures, wire an EMR-aware
DAG in a separate change, and build an idempotent Gold/merge example with
failure-injection/retry tests.
