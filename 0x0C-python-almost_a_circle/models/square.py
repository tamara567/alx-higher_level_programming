#!/usr/bin/python3
"""
The square module
Contains implementation of Square inheriting from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a square object, inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the default attributes of the Square
        Args:
           size (int): Length of one side.
           x (int): Horizontal (x) padding of the square.
           y (int): Vertical (y) padding of the square.
           id (int): Identifier
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return attributes in [Square] (<id>) <x>/<y> - <size> format
        """
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # size getter and setter.
    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the sqaure attributes.
        Args:
            args (list): positional arguments to be modified [id, width, height, x, y].
            kwargs (dict): keyword arguments to be modified.
        """
        kwarg_pairs = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args) if len(args) <= 5 else 5):
                kwarg_pairs[keys[i]] = args[i]
        else:
            kwarg_pairs = kwargs

        if len(kwarg_pairs) > 0:
            for key, value in kwarg_pairs.items():
                if key == 'id' and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
