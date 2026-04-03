from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional


@dataclass
class Log:
    page: str
    level: str
    message: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    context: Optional[Dict] = None
    trace_id: Optional[str] = None