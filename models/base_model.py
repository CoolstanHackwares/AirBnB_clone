#!/usr/bin/python3
"""Defines the class base model"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel for the AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = kwargs.get('id', str(uuid4()))
        self.created_at = self.parse_datetime(kwargs.get('created_at'))
        if kwargs.get('created_at') else datetime.today()
        self.updated_at = self.parse_datetime(kwargs.get('updated_at'))
        if kwargs.get('updated_at') else datetime.today()
        if not kwargs:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return "{}({}) {}".format(type(self).__name__, self.id, self.__dict__)

    @staticmethod
    def parse_datetime(date_string):
        """Parse a datetime string and return a datetime object."""
        if date_string:
            return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
