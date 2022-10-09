#!/usr/bin/python3
"""Displays all City obj from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


def list_city_obj():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State, City).join(City).all()

    for i in rows:
        print("{}: ({}) {}".format(i[0].__dict__['name'],
                                   i[1].__dict__['id'],
                                   i[1].__dict__['name']))

    session.close()

if __name__ == "__main__":
    list_city_obj()
