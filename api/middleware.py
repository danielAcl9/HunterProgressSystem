"""Error handling middleware"""

from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import traceback
import time
from api.logging_config import logger

async def error_handler_middleware(request: Request, call_next):
    """Middleware to catch and format errors consistently"""
    start_time = time.time()

    logger.info(f"Incoming request: {request.method} {request.url.path}")

    try:
        response = await call_next(request)

        process_time = time.time() - start_time
        logger.info(
            f"Request completed: {request.method} {request.url.path}"
            f"- Status: {response.status_code} - Time: {process_time:.3f}s"
        )

        return response

    except Exception as exc:
        # Error log
        process_time = time.time() - start_time
        logger.error(
            f"Request failed: {request.method} {request.url.path} "
            f"- Error: {str(exc)} - Time: {process_time:.3f}s",
            exc_info=True
        )

        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {
                "error": {
                    "type": "internal_server_error",
                    "message": "An unexpected error ocurred",
                    "path": str(request.url.path)
                }
            }
        )
    
def add_exception_handlers(app): 
    """Add custom exception handlers to the app"""

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """Handle HTTP exceptions with consistent format."""

        logger.warning(
            f"HTTP {exc.status_code}: {request.method} {request.url.path} - {exc.detail}"
        )
        return JSONResponse(
            status_code = exc.status_code,
            content = {
                "error": {
                    "type": "http_error",
                    "message": exc.detail,
                    "status_code": exc.status_code,
                    "path": str(request.url.path)
                }
            }
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """Handle Pydantic validation errors with consistent format."""
        errors = []
        for error in exc.errors():
            errors.append({
                "field": " -> ".join(str(loc) for loc in error["loc"]),
                "message": error["msg"],
                "type": error["type"]
            })

        logger.warning(
            f"Validation error: {request.method} {request.url.path} - "
            f"Fields: {[e['field'] for e in errors]}"
        )

        return JSONResponse(
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
            content = {
                "error": {
                    "type": "validation_error",
                    "message": "Request validation failed",
                    "details": errors,
                    "path": str(request.url.path)
                }
            }
        )