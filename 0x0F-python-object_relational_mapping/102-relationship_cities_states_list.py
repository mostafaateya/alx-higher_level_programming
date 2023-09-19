#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    X = sessionmaker(bind=engine)
    x = X()
    for a in x.query(State).order_by(State.id):
        for c_a in a.cities:
            print(c_a.id, c_a.name, sep=": ", end="")
            print(" -> " + a.name)
