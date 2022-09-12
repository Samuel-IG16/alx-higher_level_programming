#!/usr/bin/python3
"""List all State objects from db 'hbtn_0e_6_usa'
Script should take 3 args: username, pw, and db name
Must use SQLAlchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State):
        print("{:d}: {}".format(instance.id, instance.name))
