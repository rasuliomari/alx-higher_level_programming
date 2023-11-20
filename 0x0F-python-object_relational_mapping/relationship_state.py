#!/usr/bin/python3
"""
This script contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City
from sqlalchemy.orm import relationship


class State(Base):
    """
    Table states
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
