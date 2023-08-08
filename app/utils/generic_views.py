from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class Crud():
    """
    Class to Create, Read, Update, Delete
    """
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create(self, model, keys):
        new_obj = model(**keys.dict())
        try:
            self.db_session.add(new_obj)
            await self.db_session.commit()
            await self.db_session.refresh(new_obj)
            await self.db_session.flush()
        except Exception:
            await self.db_session.rollback()  # Rollback the transaction on exception
            raise  # Raise the exception to be handled at a higher level
        finally:
            await self.db_session.close()  # Close the session
        return new_obj

    async def read_one(self, model, filter_1, filter_2):
        try:
            result = await self.db_session.execute(select(model).where(filter_1 == filter_2))
            data = result.scalars().first()
        except Exception:
            await self.db_session.rollback()  # Rollback the transaction on exception
            raise  # Raise the exception to be handled at a higher level
        finally:
            await self.db_session.close()  # Close the session
        return data

    async def update(self, model, keys, id):
        try:
            q = await self.db_session.get(model, id)
            if q:
                for k, v in keys:
                    setattr(q, k, v)
                self.db_session.add(q)
                await self.db_session.commit()
                await self.db_session.refresh(q)
                await self.db_session.close()
        except Exception:
            await self.db_session.rollback()  # Rollback the transaction on exception
            raise  # Raise the exception to be handled at a higher level
        finally:
            await self.db_session.close()  # Close the session
        return q

    async def get_all(self, model, filter_1, filter_2):
        try:
            result = await self.db_session.execute(select(model).where(filter_1 == filter_2))
        except Exception:
            await self.db_session.rollback()  # Rollback the transaction on exception
            raise  # Raise the exception to be handled at a higher level
        finally:
            await self.db_session.close()  # Close the session
        return result.all()


