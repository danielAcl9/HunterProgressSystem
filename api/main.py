"""FastPAI application for Hunter System."""

from fastapi import FastAPI

app = FastAPI(
    title="Hunter Progression System",
    description="API for gamified habit tracking system",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
