#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
     __tablename__ = "cities"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete", backref="cities")

    else:    
        state_id = ""
        name = ""
