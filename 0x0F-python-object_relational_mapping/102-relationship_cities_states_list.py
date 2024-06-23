#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm.session import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    args = sys.argv[1:]
    conn_uri = f'mysql+mysqldb://{args[0]}:{args[1]}@localhost/{args[2]}'

    engine = create_engine(conn_uri)

    Base.metadata.create_all(engine)

    session = Session(engine)

    query_obj = session.query(City)\
        .join(State)\
        .order_by(City.id)\
        .all()

    for city in query_obj:
        print(f"{city.id}: {city.name} -> {city.state.name}")
