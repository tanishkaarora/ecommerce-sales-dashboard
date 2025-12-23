from pydantic import BaseModel

class SaleCreate(BaseModel):
    product_name: str
    category: str
    price: float
    quantity: int

class Sale(SaleCreate):
    id: int

    # class Config:
    #    class Config:
    #     from_attributes = True
    class Config:
      from_attributes = True



