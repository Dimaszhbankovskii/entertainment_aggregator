from sqlalchemy.ext.asyncio import AsyncSession

from models.db import async_session
from models.user import User


class UserRepository:

    def __init__(self):
        pass

    @staticmethod
    async def create_user(new_user: User) -> User:
        try:
            async with async_session() as db:
                db.add(new_user)
                await db.flush()
                await db.commit()
        except Exception as ex:
            await db.rollback()
            print(ex)
        return new_user


user_repository = UserRepository()
