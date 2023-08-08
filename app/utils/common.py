from functools import wraps

import bcrypt

from app.config.db_connect import get_db
from app.models.user_model import User
from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from app.models.user_model import User
from app.config.db_connect import async_session
from app.utils.generic_views import Crud


def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    authjwt_token_location: set = {"cookies", "headers"}
    authjwt_cookie_csrf_protect: bool = False


def authorize(func):
    """
    decorator for athentication.
    """
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        async with async_session() as session:
            try:
                Authorize = kwargs.get('Authorize')
                Authorize.jwt_required()
                current_user = Authorize.get_jwt_subject()
            except Exception as e:
                raise HTTPException(status_code=400, detail="Invalid Token")
            org = Crud(session)
            user = await org.read_one(User, User.email_id, current_user)
            if user:
                return await func(request,*args, **kwargs)
            else:
                raise HTTPException(status_code=400, detail="Invalid Token")
    return wrapper
#Email, userId, Org_id, Role1_id, Role2_id

def user_profile_dict(user):
    """
    output schema
    """
    user_dict = {}
    user_dict['email']=user.email_id
    user_dict['user_id']=user.user_id
    user_dict['location'] = user.location
    user_dict['first_name'] = user.first_name
    user_dict['last_name'] = user.last_name
    user_dict['country_code'] = user.country_code
    user_dict['phone_number'] = user.phone_number
    user_dict['role_name'] = user.role_name
    return user_dict


def check_super_admin(func):
    """
    This function is to check weather user is super admin or not to create organization.
    """
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        try:
            Authorize = kwargs.get('Authorize')
            super_admin = Authorize.get_raw_jwt()['super_admin']
        except Exception as e:
            raise HTTPException(status_code=400, detail= e )
        if super_admin:
            return await func(request, *args, **kwargs)
        else:
            raise HTTPException(status_code=400, detail="User is not authorize to create new organization")
    return wrapper