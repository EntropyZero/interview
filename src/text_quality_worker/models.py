from dataclasses import dataclass, field
from typing import Any


@dataclass
class JobMessage:
    JobType: str = "QualityScore"
    JobParameters: dict[str, Any] = field(default_factory=dict)
    WFData: dict[str, Any] = field(default_factory=dict)


@dataclass
class JobResult:
    Success: bool
    WFData: dict[str, Any] | None = None
    ErrorMessage: str | None = None