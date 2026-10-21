from pydantic import ValidationError

from text_quality_worker.models import JobMessage, JobResult
from text_quality_worker.services.text_quality import TextQuality, TextQualityConfig


class TextQualityWorker():
    """Scores OCR quality per page. Queue: worker.text_quality. JobTypes: QualityScore."""

    def run_job(self, job_message: JobMessage) -> JobResult:
        match job_message.JobType:
            case "QualityScore":
                try:
                    config = TextQualityConfig(**job_message.JobParameters)
                    job = TextQuality(config)
                except (TypeError, ValidationError) as ex:
                    return JobResult(Success=False,
                                     ErrorMessage=f"Invalid job parameters: {ex}")
                return JobResult(Success=True, WFData=job.run(job_message))
            case _:
                return JobResult(Success=False,
                                 ErrorMessage=f"Unknown JobType: {job_message.JobType}")