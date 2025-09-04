from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db

from ..users.repository import UserRepository
from .schemas import LoginForm, Token
from .utils import create_access_token, verify_password

router = APIRouter(
  prefix="/auth",
  tags=["auth"]
)

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/token")
async def token(form_data: LoginForm, db: Session = Depends(get_db) ):
  user = await UserRepository.find_by_email(form_data.email, db)

  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect username or password",
      headers={"WWW-Authenticate": "Bearer"},
    )

  if not verify_password(form_data.password, user.password):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect username or password",
      headers={"WWW-Authenticate": "Bearer"},
    )

  access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = create_access_token(
    data={"sub": user.email}, expires_delta=access_token_expires
  )
  return Token(access_token=access_token, token_type="bearer")
