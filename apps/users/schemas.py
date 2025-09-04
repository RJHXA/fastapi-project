from pydantic import BaseModel

from .models import UserType


class UserSchema(BaseModel):
  first_name: str
  last_name: str
  email: str
  password: str
  is_active: bool
  phone_number: str
  type: UserType
