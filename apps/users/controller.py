from fastapi import APIRouter, Depends, status
from .schemas import UserSchema
from sqlalchemy.orm import Session
from database import get_db
from .repository import UserRepository
from ..auth.controller import require_auth

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
async def create_user(data: UserSchema, db: Session = Depends(get_db)):
  return await UserRepository.save(data, db)

@router.get(
  "",
  status_code=status.HTTP_200_OK,
  response_model=UserSchema,
  name="user",
)
async def get_user(email: str, db: Session = Depends(get_db), _:bool = Depends(require_auth)):
  return await UserRepository.find_by_email(email, db)
