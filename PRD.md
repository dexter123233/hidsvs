# Product Requirements Document: Project Zavod
## Constrained Structured Extraction at Scale

### 1. Introduction
Project Zavod is a production-grade system designed for high-fidelity, constrained structured extraction from noisy text, specifically tailored for the high-stakes domain of AI-driven hiring and document processing.

### 2. System Architecture
The system follows a microservices architecture ensuring scalability, fault tolerance, and strict compliance.

#### 2.1 Ingestion Service
- **Function**: Entry point for raw documents.
- **GDPR Consent Management (Enhanced)**: 
    - Implements an explicit consent capture workflow at the edge.
    - Stores time-stamped consent tokens linked to candidate IDs.
    - Delivers Article 13/14 privacy notices before document upload.
    - Integration with a Consent Ledger for immutable auditing.

#### 2.2 Extraction Engine
- **Constrained Decoding**: Utilizes LLM-driven constrained decoding to eliminate regex fallbacks.
- **Validation Layer**: Uses Guardrails AI and Pydantic for strict schema enforcement.
- **Schema Decomposition**: Breaks complex nested objects into smaller sub-schemas to avoid context bottlenecks.
- **Few-Shot Selector**: Dynamic example selection using ChromaDB vector database based on input embedding similarity.
- **Retry Loop**: Error-guided loops that feed validation failures back into the prompt for correction.

#### 2.3 Schema Governance Service
- **Stateful Governance**: Manages schema versions across environments.
- **Asymmetric Cooldown Locks**: Prevents rapid oscillation of schema promotions/demotions.
- **Versioning**: Semantic versioning for all extraction schemas.

#### 2.4 Bias Auditing Service
- **Statistical Validation**: Employs Cochran's sampling formula to determine required sample sizes for validation.
- **Metrics**: Calculates Adverse Impact Ratios (AIR) and Differential Validity at a 99% Confidence Interval.
- **EEOC Alignment**: Fully aligned with Equal Employment Opportunity Commission guidelines for hiring fairness.

#### 2.5 Output Assembler
- ** candidate-Facing Explainability (Enhanced)**: 
    - Generates a "Decision Justification Report" in natural language.
    - Maps extracted fields to the specific source text spans used for the decision.
    - Provides a human-readable rationale for screening outcomes.

#### 2.6 Compliance API
- **Access Control**: Provides partitioned access to consent logs, bias audits, and explainability reports.
- **Audit Trails**: W3C Trace Context propagation for full end-to-end traceability.

### 3. Observability & Monitoring
- **OpenTelemetry (OTel)**: Implements GenAI semantic conventions for financial and operational attribution.
- **Tracing**: Integration with Arize Phoenix for prompt hashing and trace analysis.
- **Alerting**: Real-time alerts on validation failure spikes within a 900ms window.

### 4. 12-Factor App Compliance
- **Factor II (Dependencies)**: Explicit dependency isolation using containerization and Lockfiles.
- **Factor III (Config)**: Environment-specific configurations stored in environment variables; no secrets in code.
- **Factor IV (Backing Services)**: Backing services (ChromaDB, PostgreSQL, Redis) treated as attached resources.
- **Secrets Management**: Integration with AWS Secrets Manager for rotating API keys and DB credentials.

### 5. Non-Functional Requirements
- **Security**: TLS 1.3 for all transit, AES-256 for data at rest.
- **Standard**: Adheres to IEEE 830 SRS for documentation completeness.
- **Privacy**: GDPR Article 17 (Erasure) and Article 5 (Minimization) integrated into the data lifecycle.
