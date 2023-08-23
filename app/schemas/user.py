from pydantic.main import BaseModel
from pydantic.types import conint


class UserRequest(BaseModel):
    name: str
    surname: str
    age: conint(ge=14, le=150)
    city: str
    email: str


class UserResponse(BaseModel):
    name: str
    surname: str
    email: str
