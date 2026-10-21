from pydantic import BaseModel, Field

from text_quality_worker.models import JobMessage


class TextQualityConfig(BaseModel):
    """Settings for the TextQuality processor. Candidate defines the fields."""


class TextQuality:
    def __init__(self, config: TextQualityConfig) -> None:
        self.config = config

    def run(self, job_message: JobMessage) -> dict:
        """Return WFData updates. Candidate implements."""
        raise NotImplementedError