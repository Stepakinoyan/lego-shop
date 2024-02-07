import pytest
from httpx import AsyncClient

@pytest.mark.parametrize("name", [
        ("Japan Postcard"),

])
async def test_get_products(name, ac: AsyncClient):
        response = await ac.post(f"lego/products/search/{name}")
        assert response.status_code == 200