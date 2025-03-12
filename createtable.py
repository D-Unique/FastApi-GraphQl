from db.conn import engine, Base

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)




