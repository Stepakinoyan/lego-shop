from fastapi import APIRouter, Depends
from app.auth.manager import current_active_user
from app.cart.dao import CartDAO
from app.database import User


router = APIRouter(prefix="/cart", tags=["Добавление наборов в корзину"])

@router.post('/get_user_products')
async def get_user_products(user: User = Depends(current_active_user)):
        return await CartDAO.get_user_products_by_id(user=user.id) 

@router.post('/add_to_cart')
async def add_to_cart(id: int, user: User = Depends(current_active_user)):
            await CartDAO.add_to_cart_by_id(user_id=user.id, id=id)

@router.delete('/delete_user_product')
async def delete_user_product(id: int, user: User = Depends(current_active_user)):
        await CartDAO.delete_user_products_by_id(id=id, user_id=user.id)