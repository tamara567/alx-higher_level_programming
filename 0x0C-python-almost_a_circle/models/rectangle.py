#!/usr/bin/python3
"""
This is the rectangle module
It contains implementation of Rectangle inheriting from the Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a rectangle object
    Attributes:
        __width (int): Length of the width
        __height(int): Length of the height
        __x (int): The horizontal padding of the rectangle
        __y (int): The vertical padding of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the default attributes of the rectangle
        Args:
        __width (int): Length of the width
        __height(int): Length of the height
        __x (int): The horizontal padding of the rectangle
        __y (int): The vertical padding of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width getter setter.
    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height getter setter.
    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x getter setter.
    @property
    def x(self):
        """Get the x padding of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x padding of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y  getter setter.
    @property
    def y(self):
        """Get y padding of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y padding of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.height

    def display(self):
        """Visually represents rectangle are using # symbol"""
        print('\n' * self.y, end='')
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Return information about this instance of rectangle in
        [Rectangle] (<id>) <x>/<y> - <width>/<height> format
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}  - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates the rectangle attributes.
        Args:
            args (list): positional attributes to be modified [id, width, height, x, y].
            kwargs (dict): keyword attributes to be modified.
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
        """Returns the dictionary representation of a rectangle"""
        return {
            'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width,

        }
