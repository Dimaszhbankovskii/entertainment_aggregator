from pydantic.main import BaseModel
from pydantic.types import conint


class UserRequest(BaseModel):
    first_name: str
    second_name: str
    age: conint(ge=14, le=150)
    city: str
    email: str


class UserResponse(BaseModel):
    first_name: str
    second_name: str
