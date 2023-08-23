from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

import settings


engine: AsyncEngine = create_async_engine(
    url=settings.REAL_DATABASE_URL,
    future=True,
    echo=True
)

async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class Base(DeclarativeBase):
    pass
