FROM python:3.11-slim

RUN apt update && \
    apt install -y ffmpeg curl && \
    pip install yt-dlp fastapi uvicorn python-multipart && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]