from sqlalchemy import (
  Column,
  String,
  DateTime,
  Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
from database import Base
from datetime import datetime, timezone
import uuid

class User(Base):
  __tablename__ = "users"

  id: str = Column(
    UUID(as_uuid=True),
    primary_key=True,
    default=uuid.uuid4,
    unique=True,
    index=True
  )
  first_name: str = Column(String(100), nullable=False)
  last_name: str = Column(String(100), nullable=False)
  email: str = Column(String(100), nullable=False)
  password: str = Column(String(100), nullable=False)
  is_active: bool = Column(Boolean, default=True)

  created_at: datetime = Column(
    DateTime, 
    default=lambda: datetime.now(timezone.utc)
  )
  updated_at: datetime = Column(
    DateTime, 
    default=lambda: datetime.now(timezone.utc),
    onupdate=lambda: datetime.now(timezone.utc)
  )