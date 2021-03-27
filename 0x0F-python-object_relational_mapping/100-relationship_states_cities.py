#!/usr/bin/python3
"""
module for task 15
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
    new_s = State(name="California")
    new_c = City(name="San Francisco")
    new_s.cities.append(new_c)
    session.add(new_s)
    session.add(new_c)
    session.commit()
    session.close()
