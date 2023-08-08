from fastapi import APIRouter, Depends, HTTPException
import bcrypt
from app.config.db_connect import get_db
from app.schemas.user import UserSignUp, PasswordChange, UserProfile
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from app.models.user_model import User
from app.models.role_permission_model import Role
from fastapi.responses import JSONResponse
from app.utils.common import authorize, check_password, user_profile_dict
from datetime import datetime

db = next(get_db())
router = APIRouter(
    prefix="/user",
    tags=['Users']
)


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    authjwt_token_location: set = {"cookies", "headers"}
    authjwt_cookie_csrf_protect: bool = False


@AuthJWT.load_config
def get_config():
    return Settings()


def set_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    password_hash = pwhash.decode('utf8')
    return password_hash


async def user_signup(signup: UserSignUp):
    try:
        user = db.query(User).filter(User.email_id == signup.email_id).first()
        if user:
            return HTTPException(status_code=401, detail=f"{signup.email_id} already exists.")
        else:
            password = set_password(signup.password)
            obj = User(email_id=signup.email_id, password=password)
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return {'detail':f"{signup.email_id}User gets created.", "status_code":200 }
    except Exception:
        db.rollback()  # Rollback the transaction on exception
        raise  # Raise the exception to be handled at a higher level
    finally:
        db.close()


async def password_update(id, password: PasswordChange, Authorize: AuthJWT = Depends()):
    try:
        user = db.query(User).filter(User.id == id).first()
        validate_password = check_password(password.old_password, user.password)
        if validate_password and user.email_id == Authorize.get_jwt_subject():
            password = set_password(password.password)
            user.password = password
            user.is_password_reset = True
            user.password_reset_date = datetime.now()
            db.commit()
            db.refresh(user)
            db.close()
            return JSONResponse({"detail":" Password Updated Successfully","status_code":200})
        else:
            db.close()
            return HTTPException(status_code=401, detail="given current password did not match with the existing password or invalid Token")
    except Exception:
        db.rollback()  # Rollback the transaction on exception
        raise  HTTPException(status_code=400, detail= 'something went wrong')# Raise the exception to be handled at a higher level
    finally:
        db.close()


async def update_profile(user_id, profile: UserProfile,  Authorize: AuthJWT = Depends()):

    try:
        user = db.query(User).filter(User.id == user_id).first()
        data = profile.dict()
        if user and user.email_id == Authorize.get_jwt_subject():
            for k, v in data.items():
                setattr(user, k, v)
            db.commit()
            db.refresh(user)
            return JSONResponse({"detail":" Profile Updated Successfully","status_code":200})

        else:
            return HTTPException(status_code=401, detail="User does not exist")
    except Exception:
        db.rollback()  # Rollback the transaction on exception
        raise  # Raise the exception to be handled at a higher level
    finally:
        db.close()


async def get_profile(user_id, Authorize: AuthJWT = Depends()):
    try:
        user = db.query(User.email_id,
                    User.first_name,
                    User.last_name
                    ).filter(User.id == user_id).first()
        data = user_profile_dict(user)
        return data
    except Exception:
        db.rollback()  # Rollback the transaction on exception
        raise  # Raise the exception to be handled at a higher level
    finally:
        db.close()
