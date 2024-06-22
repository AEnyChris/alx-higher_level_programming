#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm.session import Session
from sqlalchemy import (create_engine)
import re


if __name__ == "__main__":
    args = sys.argv[1:]
    pattern = r"^[A-Z][a-z]+$"
    conn_uri = f'mysql+mysqldb://{args[0]}:{args[1]}@localhost/{args[2]}'

    engine = create_engine(conn_uri)

    Base.metadata.create_all(engine)

    session = Session(engine)

    if re.match(pattern, args[3]):
        query = session.query(State).order_by(State.id)
        state = query.filter(State.name == args[3]).first()
        if state:
            print(state.id)
        else:
            print("Not found")
