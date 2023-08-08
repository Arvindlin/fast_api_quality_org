from app.controller.organizations.org_level_2 import create_org_level_2, update_organization_level_2, \
    get_organization_level_2
from app.controller.organizations.org_level_3 import create_org_level_3, update_organization_level_3, \
    get_organization_level_3
from app.controller.organizations.org_level_4 import create_org_level_4, update_organization_level_4, \
    get_organization_level_4
from app.controller.organizations.org_level_5 import create_org_level_5, update_organization_level_5
from app.controller.organizations.organization import create_organization, update_organization_level_1, \
    get_organization_level_1
from app.schemas.organization import Org_level_1, Level, Org_level_2, Org_update_levels, Org_level_3, Org_level_4, \
    Org_level_5
from app.utils.common import Settings
# from autherization.login_jwt_generate import user_login, authorize
from starlette import status
from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi_jwt_auth import AuthJWT
from app.utils.common import authorize, check_super_admin


router = APIRouter()

@AuthJWT.load_config
def get_config():
    return Settings()


# @router.post("/organization_setup", status_code=status.HTTP_201_CREATED)
# @authorize
# # @check_super_admin
# async def organization_setup(request: Request, setup: Organization_level_1, Authorize: AuthJWT = Depends()):
#     """sds"""
#     return await create_organization(setup=setup, Authorize=Authorize)

@router.post("/org_level_1", status_code=status.HTTP_200_OK)
@authorize
@check_super_admin
async def organization_setup(request: Request, setup: Org_level_1, Authorize: AuthJWT = Depends()):
    """sds"""
    return await create_organization(setup=setup,  Authorize=Authorize)


@router.put("/org_level_1/{id}", status_code=status.HTTP_200_OK)
@authorize
@check_super_admin
async def organization_update(request: Request, id: int, setup: Org_level_1, Authorize: AuthJWT = Depends()):
    """sds"""
    return await update_organization_level_1(id, setup=setup,  Authorize=Authorize)


@router.get("/org_level_1/{id}", status_code=status.HTTP_200_OK)
@authorize
@check_super_admin
async def organization_update(request: Request, id: int, Authorize: AuthJWT = Depends()):
    """sds"""
    return await get_organization_level_1(id)

"""
Organization level_2 routes
"""
@router.post("/org_level_2", status_code=status.HTTP_200_OK)
@authorize
async def organization_setup(request: Request, setup: Org_level_2, Authorize: AuthJWT = Depends()):
    """sds"""
    return await create_org_level_2(setup=setup)


@router.put("/org_level_2/{id}", status_code=status.HTTP_200_OK)
@authorize
async def organization_update(request: Request, id: int, org_2: Org_update_levels, Authorize: AuthJWT = Depends()):
    """sds"""
    return await update_organization_level_2(id, org_2=org_2)


@router.get("/org_level_2/{id}", status_code=status.HTTP_200_OK)
@authorize
async def organization_update(request: Request, id: int, Authorize: AuthJWT = Depends()):
    """sds"""
    return await get_organization_level_2(id)

"""
Organization level_3 routes
"""

@router.post("/org_level_3", status_code=status.HTTP_200_OK)
@authorize
async def organization_setup(request: Request, setup: Org_level_3, Authorize: AuthJWT = Depends()):
    """sds"""
    return await create_org_level_3(setup=setup)


@router.put("/org_level_3/{id}", status_code=status.HTTP_200_OK)
@authorize
async def organization_update(request: Request, id: int, org: Org_update_levels, Authorize: AuthJWT = Depends()):
    """sds"""
    return await update_organization_level_3(id, org=org)


@router.get("/org_level_3/{id}", status_code=status.HTTP_200_OK)
@authorize
async def organization_update(request: Request, id: int, Authorize: AuthJWT = Depends()):
    """sds"""
    return await get_organization_level_3(id)


"""
Organization level_4 routes
"""

@router.post("/org_level_4", status_code=status.HTTP_200_OK)
@authorize
async def organization_setup(request: Request, setup: Org_level_4, Authorize: AuthJWT = Depends()):
    """sds"""
    return await create_org_level_4(setup=setup)


@router.put("/org_level_4/{id}", status_code=status.HTTP_200_OK)
@authorize
async def organization_update(request: Request, id: int, org: Org_update_levels, Authorize: AuthJWT = Depends()):
    """sds"""
    return await update_organization_level_4(id, org=org)


@router.get("/org_level_4/{id}", status_code=status.HTTP_200_OK)
@authorize
@check_super_admin
async def organization_update(request: Request, id: int, Authorize: AuthJWT = Depends()):
    """sds"""
    return await get_organization_level_4(id)


"""
Organization level_5 routes
"""

@router.post("/org_level_5", status_code=status.HTTP_200_OK)
@authorize
async def organization_setup(request: Request, setup: Org_level_5, Authorize: AuthJWT = Depends()):
    """sds"""
    return await create_org_level_5(setup=setup)


@router.put("/org_level_5/{id}", status_code=status.HTTP_200_OK)
@authorize
async def organization_update(request: Request, id: int, org: Org_update_levels, Authorize: AuthJWT = Depends()):
    """sds"""
    return await update_organization_level_5(id, org=org)