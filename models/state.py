#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if models.storage_type == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            cities = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
