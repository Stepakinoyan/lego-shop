from typing import List

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    formattedAmount: str


class SCart(BaseModel):
    user_id: int
    product: Product