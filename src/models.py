import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)



    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)

    def to_dict(self):
         return {}

class Starship(Base):
    __tablename__ = 'starship'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def to_dict(self):
         return {}

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship(Planet)

    def to_dict(self):
         return {}         

class FavoriteStarship(Base):
    __tablename__ = 'favorite_starship'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
    starship_id = Column(Integer, ForeignKey("starship.id"))
    starship = relationship(Starship)

    def to_dict(self):
         return {}

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'

    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship(Character)
    

    def to_dict(self):
         return {}      


         
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
