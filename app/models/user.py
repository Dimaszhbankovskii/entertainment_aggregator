import uuid
from sqlalchemy import Column, BOOLEAN, VARCHAR, Integer
from sqlalchemy.dialects.postgresql import UUID

from models.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), nullable=False, unique=True, primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR(32), nullable=False)
    surname = Column(VARCHAR(32), nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(VARCHAR(32), nullable=False)
    email = Column(VARCHAR(32), nullable=False, unique=True)
