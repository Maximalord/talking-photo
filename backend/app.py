from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI(title="Talking Photo API", version="1.0")

# Allow CORS for frontend JS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend index.html at /
@app.get("/")
async def read_index():
    return FileResponse("frontend/index.html")

# Serve static files (CSS/JS/etc)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Upload endpoint
@app.post("/jobs")
async def create_job(photo: UploadFile, text: str = Form(...)):
    try:
        file_location = f"/tmp/{photo.filename}"
        with open(file_location, "wb") as f:
            shutil.copyfileobj(photo.file, f)
        # Dummy response
        return {"job_id": "1234", "status": "success", "file_saved": file_location}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Dummy status/result endpoints
@app.get("/status/{job_id}")
async def job_status(job_id: str):
    return {"state": "done", "progress": 100, "message": "Video ready!"}

@app.get("/result/{job_id}")
async def job_result(job_id: str):
    # Placeholder video
    return {"url": "/static/sample.mp4"}
