from pydantic import BaseModel
from typing import Union


class Price(BaseModel):
    formattedAmount: str

class Attributes(BaseModel):
    rating: Union[int, float]
    ageRange: str
    pieceCount: int


class Variant(BaseModel):
    attributes: Attributes
    price: Price

class listingImages(BaseModel):
    url: str

class SLego(BaseModel):
    name: str
    listingImages: list[listingImages]
    variant: Variant

class LegoJSON(BaseModel):
    name: str
    listingImages: list
    rating: Union[int, float]
    ageRange: str
    pieceCount: int
    price: Union[int, float]