#!/usr/bin/python3
"""
Module of
classes that
define geometric
figures
"""


from models.base import Base


class Rectangle(Base):
    """
    Class that defines
    a geometric figure
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor of Rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function of width"""
        return self.__width

    @property
    def height(self):
        """Getter function of height"""
        return self.__height

    @property
    def x(self):
        """Getter function of x"""
        return self.__x

    @property
    def y(self):
        """Getter function of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter function of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter function of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter function of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter function of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
