FROM n8nio/n8n:latest

USER root
RUN apk add --no-cache yt-dlp ffmpeg
USER node

EXPOSE 5678