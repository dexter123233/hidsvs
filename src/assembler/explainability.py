from typing import List, Dict
import json

class ExplainabilityGenerator:
    """
    Generates candidate-facing explainability reports for automated decisions.
    """
    def __init__(self, llm_client):
        self.llm = llm_client

    def generate_justification(self, extraction_data: Dict, raw_text: str, schema_version: str) -> Dict:
        """
        Creates a human-readable justification for a set of extracted data.
        """
        prompt = (
            f"Based on the following raw text: {raw_text}\n"
            f"And these extracted values: {json.dumps(extraction_data)}\n"
            "Generate a neutral, professional, and explainable justification for these "
            "extractions that can be presented to the candidate. Reference specific phrases."
        )
        
        justification = self.llm.complete(prompt)
        
        return {
            "schema_version": schema_version,
            "justification": justification,
            "evidence_mapping": self._map_evidence(extraction_data, raw_text)
        }

    def _map_evidence(self, data, text) -> Dict:
        # Logic to map extracted keys to character offsets in raw text
        return {"mapping": "character_offsets_placeholder"}
