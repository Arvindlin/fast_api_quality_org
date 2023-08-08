import bcrypt
from fastapi_jwt_auth import AuthJWT
from app.schemas.user import UserSignUp
from fastapi import APIRouter, HTTPException, Depends
from datetime import timedelta
from app.utils.common import check_password
from app.models.user_model import User
from app.config.db_connect import async_session
from app.utils.generic_views import Crud


router = APIRouter(
    prefix="/user",
    tags=['Users']
)


async def user_login(signin: UserSignUp, Authorize: AuthJWT = Depends()):
    async with async_session() as session:
        org = Crud(session)
        check_email = await org.read_one(User, User.email_id, signin.email_id)
        if check_email:
            password = check_password(signin.password, check_email.password)
            if password is True:
                expires = timedelta(days=7)
                another_claims = {"first_name":check_email.first_name,"last_name":check_email.last_name,"role": 'null', "id": check_email.id, "super_admin": check_email.super_admin}
                access_token = Authorize.create_access_token(subject=str(signin.email_id),
                                                             user_claims=another_claims,
                                                             expires_time=expires)
                Authorize.set_access_cookies(access_token)
                response = HTTPException(status_code=200, detail=access_token)
                return response
            else:
                return HTTPException(status_code=400, detail="Password not matched with this email")
        else:
            return HTTPException(status_code=400, detail="User Invalid")