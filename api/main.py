"""FastAPI application for Hunter System."""

from fastapi import FastAPI
from api.routes import hunter, quests
from api.middleware import error_handler_middleware, add_exception_handlers
from api.logging_config import setup_logging, logger

setup_logging()
logger.info("Starting Hunter Progression System API...")


app = FastAPI(
    title="Hunter Progression System",
    description="API for gamified habit tracking system",
    version="1.0.0"
)

app.middleware("http")(error_handler_middleware)

add_exception_handlers(app)

app.include_router(hunter.router)
app.include_router(quests.router)

logger.info("Hunter System API started successfully.")

@app.get("/")
def root():
    """Root endpoint"""
    logger.info("Root endpoint accessed.")
    return {
        "message": "Welcome to Hunter Progression System API",
        "status": "operational",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}