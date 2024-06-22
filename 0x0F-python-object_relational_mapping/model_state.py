#!/usr/bin/python3
"""This module contains the class definition State
and an instance of Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """defines the class State inheriting from Basei
    
    Attributes:
        __tablename__ (str): the name of table in database
        id (int): unique, primary key, state id
        name (str): name of states
    
    """
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False)
    name = Column(String(128), nullable=False)
