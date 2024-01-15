#!/usr/bin/python3
"""This is the City module.
Defines the relationship of cities to state_id
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

from relationship_state import Base


class City(Base):
    """This class links to the `cities` table of our database.
    Attributes:
        id (int): id of the city.
        name (str): name of the city.
        state_id (int): id of the associated state.
    """

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
