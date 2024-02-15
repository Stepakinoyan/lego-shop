from fastapi import APIRouter
from app.lego.dao import LegoDAO


router = APIRouter(prefix='/lego', tags=["Получение данных о лего наборах"])

@router.post('/prepare')
async def prepare():
        await LegoDAO.prepare_database()

@router.post('/products')
async def get_products():
        return await LegoDAO.get_data_from_db()

@router.post('/product/{id}')
async def get_product_by_id(id: int):
        return await LegoDAO.get_lego_by_id(id)

@router.post('/products/search')
async def get_product_by_id(q: str):
        return await LegoDAO.lego_search(q)