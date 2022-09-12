#!/usr/bin/python3
"""Change name of State obj from db 'hbtn_0e_6_usa'
Change name of State where "id = 2" to "New Mexico"
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

    res = session.query(State).filter(State.id == 2)
    res.update({"name": ("New Mexico")})

    session.commit()
