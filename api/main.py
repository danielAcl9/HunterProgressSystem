"""FastPAI application for Hunter System."""

from fastapi import FastAPI
from api.routes import hunter, quests

app = FastAPI(
    title="Hunter Progression System",
    description="API for gamified habit tracking system",
    version="1.0.0"
)

app.include_router(hunter.router)
app.include_router(quests.router)

@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Hunter Progression System API",
        "status": "operational",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}