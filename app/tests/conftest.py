import json
import pytest
from sqlalchemy import insert
from config import settings
from database import Base, async_session_maker, engine

from lego.model import Lego
from httpx import AsyncClient
from main import app


@pytest.fixture(scope="session" ,autouse=True)
async def prepare_database():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
       await conn.run_sync(Base.metadata.drop_all)
       await conn.run_sync(Base.metadata.create_all)

    def open_mock_json():
        with open("app/tests/mock_lego.json", 'r') as file:
            return json.load(file) 

    lego = open_mock_json()

    async with async_session_maker() as session:
        add_lego = insert(Lego).values(lego)

        await session.execute(add_lego)

        await session.commit()


@pytest.fixture(scope="function")
async def ac():
        async with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac

@pytest.fixture(scope="function")
async def session():
    async with async_session_maker() as session:
        yield session