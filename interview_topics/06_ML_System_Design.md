# ML System Design & MLOps

## Core Concepts
- **Model Deployment:** Rest APIs, gRPC, Flask/FastAPI, Docker, Kubernetes.
- **Serving Modes:** Batch processing (offline) vs Real-time/Online inference.
- **Handling Scale:** Load balancing, caching, asynchronous queues (e.g., Celery, Kafka).
- **Monitoring & Maintenance:**
  - Data Drift (Covariate Shift).
  - Concept Drift (Relationship between features and target changes).
  - A/B Testing, Shadow Mode deployment, Canary releases.
- **Data Pipelines:** ETL/ELT, Feature Stores, Data Warehouses vs Data Lakes.

## Common Questions
1. Design a recommendation system for Netflix. (Candidate Generation, Scoring, Re-ranking)
2. How do you detect data drift in production?
3. Your real-time model is taking too long to make predictions. How do you reduce latency?
