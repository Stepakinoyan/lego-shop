from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON


class Lego(Base):
    __tablename__ = 'lego'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    listingImages: Mapped[list[dict]] = mapped_column(JSON)
    rating: Mapped[int] = mapped_column()
    ageRange: Mapped[str] = mapped_column()
    pieceCount: Mapped[int] = mapped_column()
    formattedAmount: Mapped[str] = mapped_column()