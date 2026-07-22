import logging
from datetime import datetime
from typing import Dict, Optional

class ConsentManager:
    """
    Handles GDPR Article 13/14 consent management at the ingestion edge.
    """
    def __init__(self, db_session):
        self.db = db_session
        self.logger = logging.getLogger("Zavod.ConsentManager")

    def capture_consent(self, candidate_id: str, consent_version: str, metadata: Dict) -> bool:
        """
        Captures and logs explicit candidate consent.
        """
        self.logger.info(f"Capturing consent for {candidate_id} version {consent_version}")
        
        consent_record = {
            "candidate_id": candidate_id,
            "timestamp": datetime.utcnow().isoformat(),
            "version": consent_version,
            "granted": True,
            "metadata": metadata
        }
        
        # In a real system, this would be written to an immutable ledger
        return self.db.save("consent_ledger", consent_record)

    def verify_consent(self, candidate_id: str) -> bool:
        """
        Verifies if a valid consent token exists before processing.
        """
        record = self.db.get("consent_ledger", candidate_id)
        return record is not None and record.get("granted") is True
