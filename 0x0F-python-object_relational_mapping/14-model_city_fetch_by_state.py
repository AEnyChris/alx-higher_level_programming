#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm.session import Session
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    args = sys.argv[1:]
    conn_uri = f'mysql+mysqldb://{args[0]}:{args[1]}@localhost/{args[2]}'

    engine = create_engine(conn_uri)

    Base.metadata.create_all(engine)

    session = Session(engine)

    query = session.query(State, City).order_by(City.id)
    f_query = query.filter(State.id == City.state_id).all()
    for state, city in f_query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
