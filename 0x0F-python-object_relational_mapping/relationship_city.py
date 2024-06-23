#!/usr/bin/python3
"""This module contains the class definition State
and an instance of Base = declarative_base()
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """defines the class City inheriting from Base

    Attributes:
        __tablename__ (str): the name of table in database
        id (int): unique, primary key, state id
        name (str): name of states
        state_id (int): foreign key to state.id

    """
    __tablename__ = 'cities'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
