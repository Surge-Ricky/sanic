from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DB_USER = "YOUR-USERNAME"
DB_PW = "YOUR-PASSWORD"
DB_NAME = "YOUR-DATABASE-NAME"

DATABASE_URL = f"postgresql+asyncpg://{{DB_USER}}:{{DB_PW}}@localhost/{{DB_NAME}}"

database = create_async_engine(DATABASE_URL)
async_session = sessionmaker(database, expire_on_commit=False, class_=AsyncSession)
