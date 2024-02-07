from app.lego.dao import LegoDAO
import pytest


@pytest.mark.parametrize('id', [
        (1),
        (2),
        (3)
])
async def test_get_by_id(id):
        print(await LegoDAO.get_lego_by_id(id))

@pytest.mark.parametrize('name', [
        ("Spider-Man"),
])
async def test_search(name):
        print(await LegoDAO.lego_search(name))