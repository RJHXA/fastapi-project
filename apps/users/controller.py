from fastapi import APIRouter, Depends, status
from .schemas import UserSchema
from sqlalchemy.orm import Session
from database import get_db
from .repository import UserRepository

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.post(
  "",
  status_code=status.HTTP_201_CREATED,
  response_model=UserSchema,
  name="user"
)
def create_user(data: UserSchema, db: Session = Depends(get_db)):
  return UserRepository.save(db, data)