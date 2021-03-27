#!/usr/bin/python3
"""
module for task 16
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    e = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                      format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(e)
    Session = sessionmaker(bind=e)
    session = Session()
    rows = session.query(State).order_by(State.id).all()
    for s in rows:
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("    {}: {}".format(c.id, c.name))
    session.close()
