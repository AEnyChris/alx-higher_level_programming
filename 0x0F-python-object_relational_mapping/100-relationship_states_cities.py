#!/usr/bin/python3
"""Adds a State and a City of the State
to the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    args = sys.argv[1:]
    conn_uri = f'mysql+mysqldb://{args[0]}:{args[1]}@localhost/{args[2]}'

    engine = create_engine(conn_uri)

    Base.metadata.create_all(engine)

    session = Session(engine)
    new_state = State(name="California")
    new_city = City(name="San Fransico")
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()
