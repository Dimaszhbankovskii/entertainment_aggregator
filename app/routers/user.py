from fastapi.routing import APIRouter
from fastapi.param_functions import Depends
from fastapi.requests import Request
from fastapi.responses import Response

from common import root_endpoint_v1
from schemas.user import UserRequest, UserResponse
from services.user import UserOperator, get_user_operator


router = APIRouter(
    prefix=root_endpoint_v1 + "/user",
    tags=["user"],
    responses={404: {"description": "Not found"}}
)


@router.post("", response_model=UserResponse, status_code=201)
async def create_user(user_request: UserRequest,
                      user_operator: UserOperator = Depends(get_user_operator)):
    return await user_operator.create_user(user_request)
