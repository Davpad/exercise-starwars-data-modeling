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
    favorites_persons = relationship('FavoritesPerson', backref='user', lazy=True)
    favorites_planets = relationship('FavoritesPlanet', backref='user', lazy=True)
    favorites_vehicles = relationship('FavoritesVehicle', backref='user', lazy=True)


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    lifespan = Column(Integer)
    classification = Column(String(80))
    designation = Column(String(80))
    eye_color = Column(String(80))
    hair_color = Column(String(80))
    language = Column(String(80))
    skin_color = Column(String(80))
    favorites_persons = relationship('FavoritesPerson', backref='person', lazy=True)

class FavoritesPerson(Base):
    __tablename__ = 'favorites_person'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('person.id'))


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(80))
    diameter = Column(Integer)
    gravity = Column(Integer)
    orbital_period = Column(Integer)
    population = Column(Integer)
    rotational_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String(80))
    favorites_planets = relationship('FavoritesPlanet', backref='planet', lazy=True)

class FavoritesPlanet(Base):
    __tablename__ = 'favorites_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cargo_capacity = Column(Integer)
    consumables = Column(String(80))
    cost_in_credits = Column(Integer)
    crew = Column(String(80))
    lenght = Column(Integer)
    manufacturer = Column(String(80))
    max_speed = Column(Integer)
    model = Column(String(80))
    passengers = Column(String(80))
    vehicle_class = Column(String(80))
    favorites_vehicles = relationship('FavoritesVehicle', backref='vehicle', lazy=True)   

class FavoritesVehicle(Base):
    __tablename__ = 'favorites_vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
