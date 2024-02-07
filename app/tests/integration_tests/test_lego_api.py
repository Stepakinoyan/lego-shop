from httpx import AsyncClient
import pytest

@pytest.mark.parametrize('id', [
        (1),
        (2),
        (3)
])
async def test_get_by_id(id, ac: AsyncClient):
        response = await ac.post(f"lego/product/{id}")
        assert response.status_code == 200

async def test_get_products(ac: AsyncClient):
        response = await ac.post(f"lego/products")
        assert response.status_code == 200

@pytest.mark.parametrize("name", [
        ("Japan Postcard"),
        ("Polaroid OneStep SX-70 Camera"),
        ("Flowers in Watering Can"),
        ("fjioeiorthou6o")
])
async def test_get_products(name, ac: AsyncClient):
        response = await ac.post(f"lego/products/search/{name}")
        assert response.status_code == 200