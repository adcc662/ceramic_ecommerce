from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.db.database import Base


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float, index=True)
    weight = Column(Float, index=True)
    product_category_id = Column(Integer, ForeignKey('category.id'))
    

class ProductOptions(Base):
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    option_id = Column(Integer, ForeignKey('option.id'))
    option_price_increment = Column(Float, index=True)


class Option(Base):
    id = Column(Integer, primary_key=True, index=True)
    option_name = Column(String, unique=True, index=True)


class Category(Base):
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, unique=True, index=True)


class Orders(Base):
    id = Column(Integer, primary_key=True, index=True)
    order_user_id = Column(Integer, ForeignKey('user.id'))
    order_amount = Column(Float, index=True)
    order_ship_name = Column(String, index=True)
    order_ship_address = Column(String, index=True)
    order_city = Column(String, index=True)
    order_state = Column(String, index=True)
    order_zip = Column(String, index=True)
    order_country = Column(String, index=True)
    order_phone = Column(Integer, index=True)
    order_fax = Column(Integer, index=True)
    order_shipping = Column(String, index=True)
    order_tax = Column(Float, index=True)
    order_email = Column(String, index=True)
    order_shipped = Column(Integer, index=True)
    



    