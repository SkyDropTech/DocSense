import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import upload

app = FastAPI(title="DocSense API")

# Allow requests from our frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include our upload API routes
app.include_router(upload.router)

# ==========================================
# NEW: Serve the Frontend UI directly
# ==========================================

# 1. Dynamically find the path to the 'frontend' folder
# (Goes up from app -> backend -> DocSense -> then into frontend)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# 2. Mount the CSS and JS directories so the HTML can load styles and scripts
app.mount("/css", StaticFiles(directory=os.path.join(FRONTEND_DIR, "css")), name="css")
app.mount("/js", StaticFiles(directory=os.path.join(FRONTEND_DIR, "js")), name="js")

# 3. Override the root URL to serve the index.html page instead of the JSON health check
@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))