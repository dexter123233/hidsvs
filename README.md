# Project Zavod: Constrained Structured Extraction at Scale

Zavod is a production-grade system for high-fidelity, constrained structured extraction from noisy text, designed for the AI-driven hiring domain.

## 🚀 Key Features

- **Constrained Extraction**: LLM-driven constrained decoding with Guardrails AI and Pydantic validation.
- **Schema Governance**: Stateful management with asymmetric cooldown locks to prevent configuration oscillation.
- **Bias Auditing**: Statistical validation using Cochran's formula and Adverse Impact Ratio (AIR) calculation (EEOC aligned).
- **GDPR Compliance**: Integrated consent management workflow at the ingestion edge (Article 13/14).
- **Explainability**: Natural language justification reports for automated extraction decisions.
- **Enterprise Observability**: Full OpenTelemetry (OTel) GenAI semantic tracing with Arize Phoenix.

## 🏗️ Architecture

The system is designed as a set of microservices adhering to the **12-Factor App** methodology:

- `Ingestion Service`: Handles document entry and GDPR consent.
- `Extraction Engine`: Performs the constrained extraction and retrieval-augmented few-shot selection.
- `Governance Service`: Manages schema versions and promotion/demotion logic.
- `Auditing Service`: monitors for bias and statistical validity.
- `Output Assembler`: Generates final formatted output and explainability reports.
- `Compliance API`: Centralized access for audit trails and consent logs.

## 🌐 Live Demo

The PoC app is deployed on Vercel: [https://zavod-extraction-poc.vercel.app](https://zavod-extraction-poc.vercel.app)

## 🛠️ Setup

1. Clone the repository.
2. Copy `.env.example` to `.env` and fill in your credentials.
3. Refer to `PRD.md` for detailed architectural specifications.

## 📜 Documentation

Detailed requirements and design specifications can be found in the [PRD.md](./PRD.md).
