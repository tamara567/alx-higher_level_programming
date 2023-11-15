#!/usr/bin/python3
"""
This is the base module
It contains the "base" to be used throughout the project
"""
import json


class Base():
    """
    The base of all other classes in the project.
    Used to manage the id attribute to avoid code duplication.
    Attributes:
        __nb_objects (int): Number of Base objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialized the default attributes
        Args:
            id (int): Identifier of the Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list objects to a file.
        Args:
            list_objs (list): a list of objects.
        """
        list_dictionaries = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
            dictionary (dict): the values of the target instance.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                json_file = Base.from_json_string(f.read())
                return [cls.create(**dct) for dct in json_file]
        except IOError:
            return []
