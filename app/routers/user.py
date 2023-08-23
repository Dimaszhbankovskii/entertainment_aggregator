from fastapi.routing import APIRouter
from fastapi.param_functions import Depends
from fastapi.requests import Request
from fastapi.responses import Response

from common import root_endpoint_v1
from schemas.user import UserRequest, UserResponse


router = APIRouter(
    prefix=root_endpoint_v1 + "/user",
    tags=["user"],
    responses={404: {"description": "Not found"}}
)


@router.post("", response_model=UserResponse, status_code=201)
async def create_user(user: UserRequest):
    return UserResponse(first_name=user.first_name,
                        second_name=user.second_name)
