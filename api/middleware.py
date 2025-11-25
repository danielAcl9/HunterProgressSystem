"""Error handling middleware"""

from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import traceback

async def error_handler_middleware(request: Request, call_next):
    """Middleware to catch and format errors consistently"""
    try:
        return await call_next(request)
    except Exception as exc:
        # Error log
        print(f"Unhandled error: {exc}")
        print(traceback.format_exc)

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