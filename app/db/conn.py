from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

host= os.getenv("DATABASE_HOST", 'localhost')
password=os.getenv("DATABASE_PASSWORD")
db=os.getenv("DATABASE_NAME")
port=os.getenv("DATABASE_PORT")
user=os.getenv("DATABASE_USER")

Database_url = f"mysql+aiomysql://{user}:{password}@{host}:{port}/{db}"

engine = create_async_engine(Database_url, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
