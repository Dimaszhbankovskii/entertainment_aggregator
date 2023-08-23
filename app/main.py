import uvicorn
from fastapi.applications import FastAPI
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException

from routers import user
from services.exceptions import ValidationException, ErrorException, RequestValidationException
from schemas.error import ValidationDataError, ValidationData, ErrorResponseData

app = FastAPI(title='Entertainment_aggregator')

app.include_router(user.router)


@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=400,
        content=ValidationDataError(
            error=ValidationData(
                status=400,
                type="bad-request",
                title="Your request parameters didn't validate.",
                invalid_params=exc.errors
            )
        ).model_dump()
    )


@app.exception_handler(ErrorException)
async def validation_exception_handler(request: Request, exc: ErrorException):
    return JSONResponse(
        status_code=exc.error.status,
        content=ValidationDataError(
            error=ErrorResponseData(
                status=exc.error.status,
                type=exc.error.type,
                title=exc.error.title
            )
        ).model_dump()
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    request_validator = RequestValidationException(
        errors=exc.errors(),
        body=exc.body
    )
    return JSONResponse(
        status_code=400,
        content=ValidationDataError(
            error=ValidationData(
                status=400,
                type="bad-request",
                title="Your request parameters didn't validate.",
                invalid_params=request_validator.define_invalid_params()
            )
        ).model_dump()
    )


@app.exception_handler(405)
async def validation_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=405,
        content=ValidationDataError(
            error=ErrorResponseData(
                status=405,
                type="method-not-found",
                title="The method has been disabled and can not be used."
            )
        ).model_dump()
    )


@app.exception_handler(404)
async def validation_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content=ValidationDataError(
            error=ErrorResponseData(
                status=404,
                type="not-found",
                title="Requested resource is not available."
            )
        ).model_dump()
    )


if __name__ == '__main__':
    uvicorn.run(app=app,
                host='0.0.0.0',
                port=8000)
