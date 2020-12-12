#!/usr/bin/python3
"""
module for task 14
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    e = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                      .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=e)
    ses = Session()
    for i in ses.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print("{}: ({}) {}".format(i[0], i[1], i[2]))
    ses.close()
