---

## 🧠 Engineering Decisions

This project was designed to simulate real-world data platform challenges.
Below are key architectural decisions and their rationale.

---

### ✅ Bronze/Silver Layer Separation

**Decision:**  
Raw and processed data are stored in separate layers.

**Why?**

- Preserves raw immutable data
- Enables reprocessing without data loss
- Supports auditing and lineage tracking
- Aligns with modern Lakehouse standards

This approach improves reliability and long-term scalability.

---

### ✅ Incremental Data Processing

**Decision:**  
Pipeline processes only new or updated records.

**Why?**

- Reduces compute cost
- Improves execution time
- Enables scalable batch processing
- Prevents full dataset recomputation

Essential for production-scale pipelines.

---

### ✅ Apache Spark for Transformation

**Decision:**  
Use distributed processing instead of Pandas-based transformations.

**Why?**

- Handles large-scale datasets
- Parallel execution
- Cloud-native scalability via AWS EMR
- Production-ready processing model

Designed considering future data growth.

---

### ✅ Airflow Orchestration

**Decision:**  
Pipeline execution controlled through DAG orchestration.

**Why?**

- Explicit dependency management
- Retry & failure handling
- Observability
- Scheduling automation

Mirrors enterprise data platform orchestration patterns.

---

### ✅ Data Quality Layer Before Transformation

**Decision:**  
Validate datasets before entering Silver layer.

**Why?**

- Prevents bad data propagation
- Improves trust in analytics datasets
- Enables early anomaly detection

Data reliability was prioritized over transformation speed.

---

### ✅ Modular Pipeline Design

**Decision:**  
Separate ingestion, transformation and utilities.

**Why?**

- Easier maintenance
- Independent scalability
- Reusable components
- Cleaner testing strategy

Follows Separation of Concerns principle.

---

### ✅ Logging & Observability

**Decision:**  
Centralized logging system implemented.

**Why?**

- Debugging distributed jobs
- Execution traceability
- Production monitoring readiness

Critical for real-world pipelines.

---