from app.models.products import Product, ProductOptions, Option, Category, Orders
from app.db.database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from fastapi import HTTPException, status
from app.models.products import Product, ProductOptions, Option, Category, Orders


async def create_product(product: Product, db: Session):
    """Create a new product"""
    db_product = Product(name=product.name, price=product.price, weight=product.weight, product_category_id=product.product_category_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

