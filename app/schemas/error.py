from pydantic.main import BaseModel


class ErrorData(BaseModel):
    name: str
    type: str
    reason: str


class ErrorResponseData(BaseModel):
    type: str
    title: str
    status: int


class ValidationData(BaseModel):
    type: str
    title: str
    status: int
    invalid_params: list[ErrorData]


class ValidationDataError(BaseModel):
    error: ValidationData | ErrorResponseData
