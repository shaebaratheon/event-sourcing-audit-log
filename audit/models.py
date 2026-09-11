"""
Immutable event sourcing and cryptographic audit log models.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, Optional
import hashlib
import json

@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    aggregate_id: str
    event_type: str
    actor_id: str
    payload: Dict[str, Any]
    timestamp: datetime = field(default_factory=datetime.utcnow)
    prev_hash: Optional[str] = None
    signature: Optional[str] = None

    def compute_hash(self) -> str:
        serialized = json.dumps({
            "event_id": self.event_id,
            "aggregate_id": self.aggregate_id,
            "event_type": self.event_type,
            "actor_id": self.actor_id,
            "prev_hash": self.prev_hash,
            "payload": self.payload
        }, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions

# Model expansion definitions
