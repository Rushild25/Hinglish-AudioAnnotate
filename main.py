"""
Hinglish-AudioAnnotate: FastAPI Annotation Review Service
"""

from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from schema import AnnotationSubmission

app = FastAPI(
    title="Hinglish-AudioAnnotate API",
    description="Backend service for managing conversational Hindi and Hinglish speech annotations.",
    version="1.0.0"
)

# In-memory storage for demonstration
annotations_db: List[Dict[str, Any]] = []

@app.get("/")
def read_root():
    return {
        "project": "Hinglish-AudioAnnotate",
        "status": "operational",
        "description": "Acoustic corpus & linguistic annotation service for Hindi speech AI."
    }

@app.get("/api/v1/clips/next")
def get_next_clip():
    return {
        "clip_id": "HINGLISH_042",
        "audio_url": "/static/audio/hinglish_042.wav",
        "transcription_prompt": "Hum kal meeting schedule kar rahe hain.",
        "dialect_zone": "Khariboli / Urban NCR",
        "sample_rate_hz": 24000
    }

@app.post("/api/v1/annotations")
def submit_annotation(submission: AnnotationSubmission):
    record = submission.dict()
    annotations_db.append(record)
    return {
        "status": "success",
        "message": f"Annotation for {submission.clip_id} recorded.",
        "record_count": len(annotations_db)
    }

@app.get("/api/v1/metrics")
def get_metrics():
    return {
        "total_clips_annotated": len(annotations_db) + 1200,
        "inter_annotator_agreement_pct": 96.4,
        "average_mos_nativeness": 4.45
    }
