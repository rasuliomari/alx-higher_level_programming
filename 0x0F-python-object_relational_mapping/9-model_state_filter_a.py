#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    # Create all the tables in the database
    Base.metadata.create_all(engine)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all State objects that contain the letter 'a' and sort by states.id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    # Display the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

