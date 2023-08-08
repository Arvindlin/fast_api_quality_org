from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.pool import NullPool

load_dotenv()


db_host = os.getenv('AWSRDS_DB_HOST')
port = os.getenv('AWSRDS_DB_PORT')
db_name = os.getenv('AWSRDS_DB_NAME')
password = os.getenv('AWSRDS_DB_PASSWORD')
username = os.getenv('AWSRDS_DB_USER_NAME')

# database_url = f'postgresql+psycopg2://{db_username}:{db_password}@{db_host}/{db_name}'

database_url = f"mysql+pymysql://{username}:{password}@{db_host}:{port}/{db_name}"
# database_url = 'mysql+mysqlconnector://root@localhost:3306/sys'
# engine = create_engine(database_url, convert_unicode=True, poolclass=NullPool)
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
connection = engine.connect()

async_database_url = f"mysql+asyncmy://{username}:{password}@{db_host}:{port}/{db_name}"
async_engine = create_async_engine(async_database_url, future=True)

async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()