#!/usr/bin/python3
"""List first State objects from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_first_state_obj():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    f = session.query(State).first()

    if f:
        print("{}: {}".format(f.__dict__['id'], f.__dict__['name']))
    else:
        print("Nothing")

    session.close()

if __name__ == "__main__":
    list_first_state_obj()
