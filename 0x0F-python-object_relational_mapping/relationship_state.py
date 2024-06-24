#!/usr/bin/python3
"""This module contains the class definition State
and an instance of Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """defines the class State inheriting from Base

    Attributes:
        __tablename__ (str): the name of table in database
        id (int): unique, primary key, state id
        name (str): name of states
        cities (:obj:`City`): Cities of States

    """
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
