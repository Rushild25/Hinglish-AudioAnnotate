# Hinglish-AudioAnnotate 🎧

**Acoustic Corpus & Linguistic Annotation Platform for Conversational Hindi & Code-Switched Speech**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-green.svg)](https://fastapi.tiangolo.com/)
[![Speech Processing](https://img.shields.io/badge/Audio-Praat%20%26%20SoundFile-orange)](https://github.com/Rushild25/Hinglish-AudioAnnotate)

**Hinglish-AudioAnnotate** is a specialized framework and data curation platform for annotating conversational Hindi audio, with a targeted emphasis on intra-sentential code-switching (Hinglish), loanword phonology, and bilingual speech synthesis evaluation.

---

## 📌 Background & Motivation

Conversational Indic speech frequently weaves English technical and colloquial loanwords into Hindi syntactic frames. Generic ASR and TTS models often exhibit:
- Unnatural pitch resets at language boundaries.
- Artificial hyper-foreignization or incorrect Devanagari G2P mapping on loanwords.
- Inconsistent cadence and stress shifts.

This repository provides tooling, data schemas, and review endpoints to annotate and audit conversational Hindi audio with structured English linguistic justifications.

---

## 🚀 Key Modules

- **Boundary Intonation Tagger**: Identifies transition points between Hindi matrix clauses and English embedded phrases.
- **Phonetic Assimilation Scorer**: Measures how naturally English loanwords are adapted into Hindi phonetic flow.
- **Annotation Review API**: A lightweight FastAPI service to log evaluations, calculate inter-annotator agreement, and export ML-ready JSON datasets.
- **MOS & Defect Taxonomy**: Granular scoring rubrics for cadence, vowel reduction, and synthetic distortions.

---

## 🛠️ API & Quickstart

### Setup

```bash
git clone https://github.com/Rushild25/Hinglish-AudioAnnotate.git
cd Hinglish-AudioAnnotate
pip install -r requirements.txt
```

### Running the Annotation Service

```bash
uvicorn main:app --reload --port 8000
```

### Sample Annotation Submission

```bash
curl -X POST "http://localhost:8000/api/v1/annotations" \
  -H "Content-Type: application/json" \
  -d '{
    "clip_id": "HINGLISH_042",
    "transcription": "Hum kal meeting schedule kar rahe hain.",
    "code_switching_boundary_valid": true,
    "nativeness_score": 4.5,
    "english_feedback": "Seamless prosodic transition at loanword boundary. Natural Hindi auxiliary verb enunciation."
  }'
```

---

## 📂 Repository Structure

- `main.py`: FastAPI application serving annotation queue and metrics.
- `schema.py`: Pydantic data models for annotation records and linguistic metrics.
- `requirements.txt`: Required Python dependencies.
