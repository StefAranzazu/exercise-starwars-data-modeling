import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"))

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user = relationship("User")
      

class Characters(Base):
    __tablename__='characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable= False)
    birthday = Column(String(250), nullable = False)
    gender = Column(String(250), nullable = False)
    favorite_id = Column(Integer, ForeignKey('Favorite.id'))
    favorite= relationship("Favorite")

class Planets(Base):
    __tablename__='planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable= False)
    populations= Column(String(250), nullable= False)
    diameter= Column(String(250), nullable= False)
    favorite_id = Column(Integer, ForeignKey('Favorite.id'))
    favorite= relationship("Favorite")
    



   
    
    

 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')