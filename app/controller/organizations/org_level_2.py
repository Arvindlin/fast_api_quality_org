from app.config.db_connect import async_session
from app.models.organization_model import Organization_level_2, Organization, Organization_level_3
from app.schemas.organization import Org_level_2, Org_update_levels
from app.utils.generic_views import Crud
from fastapi import  HTTPException


async def create_org_level_2(setup: Org_level_2):
    """
    create level 2 data
    """
    async with async_session() as session:
        new_org = Crud(session)
        data = await new_org.create(Organization_level_2, setup)
        await session.close()
        return {"status_code":200,
                "msg": f"{setup.level_name} level 2 org gets created.",
                "detail": data}


async def  update_organization_level_2(id, org_2: Org_update_levels):
    """
        update level 2 data
    """
    async with async_session() as session:
        new_org = Crud(session)
        data = await new_org.update(Organization_level_2, org_2, id)
        if data:
            return {"status_code":200,
                "msg": f"{org_2.level_name} level 2 org gets updated.",
                "detail": data}
        else:
            raise HTTPException(status_code=401, detail="no data available for given id")


async def get_organization_level_2(id):
    """
        Get organization level_2 data
    """
    async with async_session() as session:
        try:
            org = Crud(session)
            data = await org.read_one(Organization_level_2, Organization_level_2.id, id)
            result = await org.get_all(Organization_level_3, Organization_level_3.organization_id, id)
            org_3 = [data._asdict()['Organization_level_3'] for data in result]
            await session.close()
        except Exception:
            await session.rollback()  # Rollback the transaction on exception
            raise  HTTPException(status_code=401, detail="Some error occured in Query")# Raise the exception to be handled at a higher level
        finally:
            await session.close()

        return {"status_code":200,
                "msg": f"{Organization_level_2.organization_name} details",
                "detail": {'org_2':data, 'org_3':org_3}}