#!/usr/bin/python3
"""Print State obj with 'name' passed as arg from db 'hbtn_0e_6_usa'
Script should take 4 args: username, pw, db name, and state name
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

    res = session.query(State.id).filter(State.name == sys.argv[4])

    if (res.first() is None):
        print("Not found")
    else:
        print(res[0][0])
