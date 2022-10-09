#!/usr/bin/python3
"""Updates into State obj from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def update_to_state_obj():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    to_change = session.query(State).filter(State.id == 2).first()

    to_change.name = 'New Mexico'
    session.commit()

    session.close()

if __name__ == "__main__":
    update_to_state_obj()
