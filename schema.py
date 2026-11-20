"""
Hinglish-AudioAnnotate: Data Models & Annotation Schemas
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class DefectType(str, Enum):
    PITCH_RESET = "pitch_reset"
    SCHWA_FAILURE = "schwa_failure"
    ASPIRATION_LOSS = "aspiration_loss"
    SYNTHETIC_GLITCH = "synthetic_glitch"
    UNNATURAL_CADENCE = "unnatural_cadence"

class AnnotationSubmission(BaseModel):
    clip_id: str
    transcription: str
    code_switching_boundary_valid: bool = True
    nativeness_score: float = Field(..., ge=1.0, le=5.0)
    pronunciation_score: float = Field(..., ge=1.0, le=5.0)
    intonation_score: float = Field(..., ge=1.0, le=5.0)
    detected_defects: List[DefectType] = []
    english_feedback: str
    annotator_id: Optional[str] = "expert_hi_evaluator"
