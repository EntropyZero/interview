# Han — Jr. Data Scientist Tech Screen (Wed Oct 21, 10:30–12:30, pairing)

**Format:** paired coding session on a Python HybridBus worker. Candidate writes ~70%, Steven narrates/questions. Repo context is real (to-hybridbus-workers pattern) but the task is self-contained — no RabbitMQ, no HB certs, no Tesseract needed. Runs with just `uv` + pytest.

## What we're hiring for

Junior DS who can: take an ambiguous spec about data, pick sane thresholds/representations with reasoning, handle missing/dirty data without crashing, and let tests define "done." The worker framing is a vehicle; we're watching data judgment, not MQ knowledge.

## The task

**TextQualityWorker** — a new Python worker in the HybridBus worker style.

Upstream OCR writes per-page results to `WFData["ocr_pages"]`: a list with one entry per page, in page order. Each entry is a dict with exactly these fields:

| Field | Type | Meaning |
|---|---|---|
| `page` | `int` | 1-based page number |
| `words` | `list[[str, float]]` | One pair per recognized word: the word's text, and the OCR engine's confidence in that word on a **0–100** scale |
| `text` | `str` | The page's reconstructed text — in practice the words joined with spaces, but not guaranteed to match `words` exactly (spacing/casing may drift) |

A two-page document, in full:
```json
[
  {
    "page": 1,
    "words": [["injured", 96.4], ["party", 91.0], ["was", 87.2]],
    "text": "injured party was"
  },
  {
    "page": 2,
    "words": [["tiff", 31.5], ["ane", 28.9], ["mar", 44.0]],
    "text": "tiff ane mar"
  }
]
```

Page 2 is what a bad scan looks like. That shape is what upstream *usually* produces; degraded pages happen.

Build a worker with JobType `"QualityScore"` that scores each page's OCR quality and writes a summary to `WFData["workflow_result"]["quality"]`, including a per-page `needs_review` flag so downstream routing can pull suspect pages for human review.

How to score, what `needs_review` means, and what to do with weird input are your call — tell me your reasoning as you choose.

