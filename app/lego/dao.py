import json
from sqlalchemy import insert, select
from app.dao.dao import BaseDAO
from app.lego.model import Lego
from app.database import async_session_maker


class LegoDAO(BaseDAO):
    model = Lego

    async def prepare_database():

        def open_mock_json():
            with open("app/tests/mock_lego.json", 'r') as file:
                return json.load(file) 

        lego = open_mock_json()

        async with async_session_maker() as session:
            add_lego = insert(Lego).values(lego)

            await session.execute(add_lego)

            await session.commit()

    @classmethod
    async def get_data_from_db(self):
        async with async_session_maker() as session:
            get_data = select(self.model.__table__.columns)

            result = await session.execute(get_data)

            return result.mappings().all()
        
    @classmethod
    async def get_lego_by_id(self, id: int):
        async with async_session_maker() as session:
            get_by_id = select(self.model.__table__.columns).where(self.model.id == id)

            result = await session.execute(get_by_id)

            return result.mappings().all()
        
    @classmethod
    async def lego_search(self, name: str):
            async with async_session_maker() as session:
                if name.count(' ') >= 1:
                     search = select(self.model.__table__.columns).where(self.model.name.like(f"%{name}%"))
                else:
                    search = select(self.model.__table__.columns).where(self.model.name.like(f"%{name.capitalize()}%"))


                result = await session.execute(search)
                return result.mappings().all()