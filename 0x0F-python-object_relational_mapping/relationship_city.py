#!/usr/bin/python3
"""
file model similar to model_state.py named model_city.py
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Data base operation
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
