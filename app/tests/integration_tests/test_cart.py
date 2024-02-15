from cart.dao import CartDAO


async def test_add_to_cart():
    await CartDAO.add_to_cart_by_id(2, 1)

async def test_get_user_products_by_id():
    print(await CartDAO.get_user_products_by_id(1))