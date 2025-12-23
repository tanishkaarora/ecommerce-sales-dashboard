from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce Sales API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/sales")
def add_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    new_sale = models.Sale(**sale.dict())
    db.add(new_sale)
    db.commit()
    return {"message": "Sale added"}

# @app.get("/sales")
# def get_sales(db: Session = Depends(get_db)):
#     return db.query(models.Sale).all()
from typing import List

@app.get("/sales", response_model=List[schemas.SaleCreate])
def get_sales(db: Session = Depends(get_db)):
    return db.query(models.Sale).all()

@app.get("/")
def home():
    return {"message": "E-Commerce Sales API is running"}
