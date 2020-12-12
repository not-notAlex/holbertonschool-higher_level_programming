#!/usr/bin/python3
"""
module for task 10
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    e = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                      .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=e)
    ses = Session()
    found = 0
    for i in ses.query(State).order_by(State.id):
        if i.name == argv[4]:
            print("{}: {}".format(i.id, i.name))
            found = 1
    if found == 0:
        print("Not found")
    ses.close()
