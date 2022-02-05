import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, Date, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Web user data
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(15), nullable=False)
    active = Column(Integer, default=0)

# Existing data types (Planet, Vehicle, Character...)
class DataType(Base):
    __tablename__ = "data_type"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    temperature = Column(Float)

class Vehicle_Brand(Base):
    __tablename__ = "vehicle_brand"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float)
    brand_id = Column(Integer, ForeignKey("vehicle_brand.id"))
    brand = relationship(Vehicle_Brand)

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birthday = Column(Date, nullable=False)
    planet_id = Column(Integer, ForeignKey("planet.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    planet = relationship(Planet)
    vehicle = relationship(Vehicle)

# List of all user favourites
class Favourite(Base):
    __tablename__ = "favourite"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    data_type_id = Column(Integer, ForeignKey("data_type.id"), primary_key=True)
    data_id = Column(Integer, primary_key=True)
    
## Draw from SQLAlchemy base
render_er(Base, "diagram.png")
