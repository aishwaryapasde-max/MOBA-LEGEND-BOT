FROM python:3.9-slim

# System dependencies for the bot
RUN apt-get update && apt-get install -y \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# Render par chalu karne ki command
CMD xvfb-run gunicorn main:app
