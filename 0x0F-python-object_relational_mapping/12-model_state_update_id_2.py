#!/usr/bin/python3
"""
module for task 12
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
    nm = ses.query(State).filter_by(id=2).first()
    nm.name = "New Mexico"
    ses.commit()
    ses.close()
