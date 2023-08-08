from fastapi import  HTTPException

from app.config.db_connect import async_session
from app.models.organization_model import Organization_level_5, Organization_level_4
from app.schemas.organization import Org_level_5, Org_update_levels
from app.utils.generic_views import Crud


async def create_org_level_5(setup: Org_level_5):
    """
    create level 2 data
    """
    async with async_session() as session:
        new_org = Crud(session)
        data = await new_org.create(Organization_level_5, setup)
        await session.close()
        return {"status_code": 200,
                "msg": f"{setup.level_name} level 5 org gets created.",
                "detail": data}


async def  update_organization_level_5(id, org: Org_update_levels):
    """
        update level 4 data
    """
    async with async_session() as session:
        new_org = Crud(session)
        data = await new_org.update(Organization_level_5, org, id)
        if data:
            return {"status_code": 200,
                "msg": f"{org.level_name} level 5 org gets updated.",
                "detail": data}
        else:
            raise HTTPException(status_code=401, detail="no data available for given org")


# async def get_organization_level_5(id):
#     """
#         Get organization level_4 data
#     """
#     async with async_session() as session:
#         try:
#             org = Crud(session)
#             data = await org.read_one(Organization_level_4, Organization_level_4.id, id)
#             result = await org.get_all(Organization_level_5, Organization_level_5.organization_id, id)
#             org_5 = [data._asdict()['Organization_level_3'] for data in result]
#             await session.close()
#         except Exception:
#             await session.rollback()  # Rollback the transaction on exception
#             raise HTTPException(status_code=401,
#                                 detail="Some error occured in Query")  # Raise the exception to be handled at a higher level
#         finally:
#             await session.close()
#
#         return {"status_code": 200,
#                 "msg": f"{Organization_level_3.organization_name} details",
#                 "detail": {'org_3': data, 'org_5': org_5}}