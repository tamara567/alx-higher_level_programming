#!/usr/bin/python3
"""
Add "Louisiana" state to the db
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()

    new_state = State(name="Louisiana")
    s.add(new_state)
    s.commit()
    print(new_state.id)
