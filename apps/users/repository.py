from sqlalchemy.orm import Session
from .schemas import UserSchema
from .models import User
from ..auth.utils import get_hash_password

class UserRepository:
  @staticmethod
  async def save(user_data: UserSchema, db: Session):
    user = User(
      first_name=user_data.first_name,
      last_name=user_data.last_name,
      email=user_data.email,
      phone_number=user_data.phone_number,
      password=get_hash_password(user_data.password),
      type=user_data.type
    )

    db.add(user)

    db.commit()
    return user
  
  @staticmethod
  async def find_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()
