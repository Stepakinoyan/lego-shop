from sqlalchemy import and_, delete, insert, select
from app.cart.model import Cart
from app.cart.schema import SCart
from app.dao.dao import BaseDAO
from app.lego.dao import LegoDAO
from app.database import async_session_maker


class CartDAO(BaseDAO):
    model = Cart

    @classmethod
    async def add_to_cart_by_id(self, user_id: int, id: int):
        lego = await LegoDAO.get_lego_by_id(id)
        scart = SCart(product=lego[0], user_id=user_id).model_dump()
   
        async with async_session_maker() as session:
            insert_to_cart = insert(Cart).values(scart)
            result = await session.execute(insert_to_cart)
            await session.commit()
    
    @classmethod
    async def get_user_products_by_id(self, user: int):
        async with async_session_maker() as session:
            get_user_products = select(self.model.__table__.columns).where(self.model.user_id == user)
            result = await session.execute(get_user_products)
            return result.mappings().all()
        
    @classmethod
    async def delete_user_products_by_id(self, id: int, user_id: int):
        async with async_session_maker() as session:
            delete_user_products = delete(self.model).where(
                and_(self.model.id) == id,
                and_(self.model.user_id == user_id)
            ) 
                                        
            result = await session.execute(delete_user_products)
            await session.commit()