from typing import List, Optional

from pydantic import BaseModel, EmailStr
from pydantic.types import constr
from app.schemas.validation import Validation


class UserSignUp(BaseModel):
    email_id: constr(strict=True, strip_whitespace=True, regex=Validation.EMAIL_REGEX)
    password: constr(strict=True, min_length=8, max_length=16, regex=Validation.password_pattern)

    class Config:
        orm_mode = True


class PasswordChange(BaseModel):
    old_password: constr(strict=True, min_length=8, max_length=16, regex=Validation.password_pattern)
    password: constr(strict=True, min_length=8, max_length=16, regex=Validation.password_pattern)

    class Config:
        orm_mode = True


class UserProfile(BaseModel):
    # country_id: constr(max_length=5)
    # phone_no: constr(strict=True, min_length=10, max_length=16)
    first_name: constr(strict=True)
    last_name: Optional[str]

    class Config:
        orm_mode = True

