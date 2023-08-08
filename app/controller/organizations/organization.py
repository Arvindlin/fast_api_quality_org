from app.models.organization_model import Organization, Organization_level_2
from app.schemas.organization import Org_level_1
from fastapi import APIRouter, HTTPException, Depends
from app.config.db_connect import async_session
from app.utils.generic_views import Crud
from sqlalchemy.future import select
from fastapi_jwt_auth import AuthJWT


router = APIRouter(
    prefix="/user",
    tags=['Users']
)


async def create_organization(setup: Org_level_1, Authorize: AuthJWT = Depends()):
    """
        to create organization level 0
    """
    async with async_session() as session:
        new_org = Crud(session)
        data = await new_org.read_one(Organization, Organization.organization_name, setup.organization_name)
        if data:
            await session.close()
            raise HTTPException(status_code=401, detail=f"{setup.organization_name} organization already exists.")
        else:
            data = await new_org.create(Organization, setup)
            await session.close()
            return {"msg": f"{setup.organization_name} level 1 gets created.",
                    "detail": data,
                    "status_code":200}


async def update_organization_level_1(id, setup: Org_level_1, Authorize: AuthJWT = Depends()):
    """
        Update the level 1 organization data
    """
    async with async_session() as session:
        new_org = Crud(session)
        data = await new_org.update(Organization, setup, id)
        await session.close()
        if data:
            return {"msg": f"{setup.organization_name} level 1 gets updated.",
                "detail": data,
                "status_code":200}
        else:
            raise HTTPException(status_code=401, detail="no data available for given id")


async def get_organization_level_1(id):
    """
        Get organization level1 data
    """
    async with async_session() as session:
        try:
            org = Crud(session)
            data = await org.read_one(Organization, Organization.id, id)
            result = await org.get_all(Organization_level_2, Organization_level_2.organization_id, id)
            org_2 = [data._asdict()['Organization_level_2'] for data in result]
            await session.close()
        # try:
        #     result = await session.execute(select(Organization_level_2
        #                                           ).where(Organization_level_2.organization_id == id))
        #     org_2 = [data._asdict() for data in result.all()]
        #
        except Exception:
            await session.rollback()  # Rollback the transaction on exception
            raise  HTTPException(status_code=401, detail="Some error occured in Query")# Raise the exception to be handled at a higher level
        finally:
            await session.close()

        return {"status_code":200,
                "msg": f"{Organization.organization_name} details",
                "detail": {'org':data, 'org_2':org_2}}
