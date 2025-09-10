# Simplified demo backend (copied from project) - safe to publish
# Original: simple_backend.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(title="Demo backend")

@app.get("/")
async def root():
    html_content = f"<html><body><h1>Demo</h1><p>Timestamp: {datetime.now()}</p></body></html>"
    return HTMLResponse(content=html_content)
