import pytest
from httpx import AsyncClient, ASGITransport
from tortoise import Tortoise
from api_service.src.main import app

DB_URL = "sqlite://:memory:"


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="module")
async def init_db():
    await Tortoise.init(
        db_url=DB_URL,
        modules={"models": ["api_service.src.models"]},
        _create_db=True
    )
    await Tortoise.generate_schemas()

    yield

    await Tortoise._drop_databases()


@pytest.fixture(scope="module")
async def client(init_db):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
