#!/usr/bin/python3
"""List all State objects containing argument from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_arg_state_obj():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State).all()

    res = ""

    for i in rows:
        if sys.argv[4] in i.__dict__['name']:
            res = i.__dict__['id']

    if res != "":
        print(res)
    else:
        print("Not Found")

    session.close()

if __name__ == "__main__":
    list_arg_state_obj()
