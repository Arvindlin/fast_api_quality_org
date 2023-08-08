from app.config.db_connect import get_db
from app.main import app
from fastapi import Request


@app.middleware("http")
async def close_db_session(request: Request, call_next):
    response = await call_next(request)
    db = get_db()
    try:
        db.close()
    except:
        db.rollback()
        db.close()
    finally:
        return response

