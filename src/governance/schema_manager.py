import time
from typing import Dict

class SchemaGovernanceService:
    """
    Stateful schema governance with asymmetric cooldown locks.
    """
    def __init__(self):
        self.schemas = {} # schema_id -> version
        self.locks = {}   # schema_id -> last_change_timestamp
        self.COOLDOWN_PROMOTION = 3600 # 1 hour
        self.COOLDOWN_DEMOTION = 86400  # 24 hours (Asymmetric)

    def promote_schema(self, schema_id: str, version: str) -> bool:
        if self._is_locked(schema_id, self.COOLDOWN_PROMOTION):
            return False
        
        self.schemas[schema_id] = version
        self.locks[schema_id] = time.time()
        return True

    def demote_schema(self, schema_id: str, version: str) -> bool:
        if self._is_locked(schema_id, self.COOLDOWN_DEMOTION):
            return False
            
        self.schemas[schema_id] = version
        self.locks[schema_id] = time.time()
        return True

    def _is_locked(self, schema_id: str, cooldown: int) -> bool:
        last_change = self.locks.get(schema_id)
        if not last_change:
            return False
        return (time.time() - last_change) < cooldown
