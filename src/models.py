import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favoritesPerson = relationship('FavoritesPerson', backref='user', lazy=True)
    favorites = relationship('favorites', backref='user', lazy=True)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites = relationship('FavoritesPerson', backref='person', lazy=True)

class FavoritesPerson(Base):
    __tablename__ = 'favorites_person'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'),nullable = False)
    person = relationship(Person)
    user_id = Column(Integer, ForeignKey('user.id'),nullable = False)
    user = relationship(User)    

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites = relationship('favoritesPlanet', backref='planet', lazy=True)

class FavoritesPlanet(Base):
    __tablename__ = 'favorites_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'),nullable = False)
    planet = relationship(Planet)
    user_id = Column(Integer, ForeignKey('user.id'),nullable = False)
    user = relationship(User)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites = relationship('favorites', backref='vehicle', lazy=True)   

class FavoritesVehicle(Base):
    __tablename__ = 'favorites_vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'),nullable = False)
    vehicle = relationship(Vehicle)
    user_id = Column(Integer, ForeignKey('user.id'),nullable = False)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
