#!/usr/bin/python3
"""Add the State object "Louisiana" to db 'hbtn_0e_6_usa'
Print the new 'states.id' after creation
Script should take 3 args: username, pw, and db name
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

    state = State(name='Louisiana')
    session.add(state)
    session.commit()

    print(state.id)
