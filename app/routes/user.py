from pydantic import BaseModel
from app.utils.common import Settings
# from autherization.login_jwt_generate import user_login, authorize
from starlette import status
from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi_jwt_auth import AuthJWT

from app.controller.users.authentication import user_login
from app.controller.users.user_register import user_signup, password_update, update_profile, get_profile
from app.schemas.user import UserSignUp, PasswordChange, UserProfile
from app.utils.common import authorize

router = APIRouter()


@AuthJWT.load_config
def get_config():
    return Settings()


@router.get("/{id}", status_code=status.HTTP_200_OK)
@authorize
async def get_user_profile(request: Request, id : int, Authorize: AuthJWT = Depends()):
    """sds"""
    return await get_profile(user_id=id ,Authorize=Authorize)


@router.put("/{id}", status_code=status.HTTP_200_OK)
@authorize
async def update_user_profile(request: Request, id: int, profile: UserProfile, Authorize: AuthJWT = Depends()):
    """sds"""
    return await update_profile(user_id=id, profile=profile, Authorize=Authorize)



@router.post("/sign_up", status_code=status.HTTP_201_CREATED)
async def user_register(request: Request, signup: UserSignUp):
    """sds"""
    return await user_signup(signup=signup)


@router.post("/log_in", status_code=status.HTTP_200_OK)
async def user_login_token(request: Request, signin: UserSignUp, Authorize: AuthJWT = Depends()):
    """sds"""
    return await user_login(signin=signin, Authorize=Authorize)


@router.put("/chnge_pswd/{id}", status_code=status.HTTP_200_OK)
@authorize
async def user_password_update(request: Request, id: int, password: PasswordChange, Authorize: AuthJWT = Depends()):
    """sds"""
    return await password_update(id=id, password=password, Authorize=Authorize)



@router.get("/me", status_code=status.HTTP_200_OK)
@authorize
async def user_me(request: Request, Authorize: AuthJWT = Depends()):
    """To check the AWT user """
    return f"welcome {Authorize.get_jwt_subject()}"
