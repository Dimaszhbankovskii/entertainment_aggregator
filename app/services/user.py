from repositories.user import user_repository
from models.user import User
from schemas.user import UserRequest, UserResponse


def get_user_operator():
    return UserOperator()


class UserOperator:

    def __init__(self):
        self.user_repository = user_repository

    async def create_user(self, user_request: UserRequest) -> UserResponse:
        new_user = User(
            name=user_request.name,
            surname=user_request.surname,
            age=user_request.age,
            city=user_request.city,
            email=user_request.email
        )
        new_user = await self.user_repository.create_user(new_user)
        return UserResponse(name=new_user.name,
                            surname=new_user.surname,
                            email=new_user.email)
