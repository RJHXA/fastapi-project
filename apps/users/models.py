import uuid
from datetime import UTC, datetime
from enum import Enum

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy import Enum as Db_Enum
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class UserType(Enum):
  ADMIN = "ADMIN"
  NORMAL = "NORMAL"

class User(Base):
  __tablename__ = "users"

  id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
  first_name: str = Column(String(100), nullable=False)
  last_name: str = Column(String(100), nullable=False)
  email: str = Column(String(100), unique=True, index=True, nullable=False)
  phone_number: str = Column(String(100), nullable=False)
  password: str = Column(String(100), nullable=False)
  is_active: bool = Column(Boolean, default=True)
  type: UserType = Column(Db_Enum(UserType), default=UserType.NORMAL)

  created_at: datetime = Column(
    DateTime,
    default=lambda: datetime.now(UTC)
  )
  updated_at: datetime = Column(
    DateTime,
    default=lambda: datetime.now(UTC),
    onupdate=lambda: datetime.now(UTC)
  )
