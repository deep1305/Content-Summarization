import subprocess
import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from content_summarization.pipeline.prediction import PredictionPipeline

app = FastAPI(title="Content Summarization API")
pipeline = PredictionPipeline()


class SummarizeRequest(BaseModel):
    text: str

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train():
    try:
        # Runs pipeline stages in main.py (trainer is skipped by your flag).
        subprocess.run(
            [sys.executable, "main.py"],
            check=True,
            cwd=Path(__file__).resolve().parent,
        )
        return {"message": "Pipeline run completed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline run failed: {e}")


@app.post("/predict")
async def predict(request: SummarizeRequest):
    try:
        summary = pipeline.predict(request.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")