from sqlalchemy.orm import Session
from .schemas import UserSchema
from .models import User

class UserRepository:
  @staticmethod
  def save(db: Session, user_data: UserSchema):
    user = User(
      first_name=user_data.first_name,
      last_name=user_data.last_name,
      email=user_data.email,
      password=user_data.password
    )

    db.add(user)

    db.commit()
    return user