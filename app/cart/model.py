from sqlalchemy import JSON
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Cart(Base):
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    product = mapped_column(JSON)