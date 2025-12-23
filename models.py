from sqlalchemy import Column, Integer, String, Float
from database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
