## Data Flow

1. Airflow triggers ingestion DAG
2. API data is extracted via Python
3. Raw data stored in Bronze layer
4. Spark job processes distributed transformations
5. Cleaned datasets written to Silver layer

## AI Enrichment Layer

An additional AI processing layer enriches curated datasets using
LLM-based classification techniques, preparing data for downstream
machine learning and intelligent applications.