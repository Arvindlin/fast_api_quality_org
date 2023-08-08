import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config.db_connect import engine
from app.models import model
from app.routes import user, organization

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# model.Base.metadata.create_all(bind=engine)        #to create tables in databse. will remove later

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user.router, prefix='/api/v1/user', tags=['Users'])
app.include_router(organization.router, prefix='/api/v1/org', tags=['Organization'])

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)


