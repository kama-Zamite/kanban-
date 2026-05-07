from ..core.settings import Settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine(Settings().BASE_URL)

async def get_session():
    async with AsyncSession(engine) as session:
        yield session


