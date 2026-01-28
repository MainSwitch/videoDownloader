from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse
import subprocess
import uuid
import os

app = FastAPI()

DOWNLOAD_DIR = "/tmp"

@app.post("/download")
def download(url: str = Form(...)):
    filename = f"{uuid.uuid4()}.mp4"
    filepath = os.path.join(DOWNLOAD_DIR, filename)

    cmd = [
        "yt-dlp",
        "-f", "mp4",
        "-o", filepath,
        url
    ]

    result = subprocess.run(cmd, capture_output=True)

    if result.returncode != 0:
        raise HTTPException(
            status_code=400,
            detail=result.stderr.decode()
        )

    return FileResponse(
        filepath,
        media_type="video/mp4",
        filename="video.mp4"
    )
