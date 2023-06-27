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

    @width.setter
    def width(self, value):
        """Setter function of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter function of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter function of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function that calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Function that prints the rectangle"""
        for i in range(self.__height):
            for e in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Overriding the str method"""
        return f"""[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"""

    def display(self):
        """Print the rectangle in a cartesian plane"""
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        """Function that updates attributes of an instance"""
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.__width = args[1]
            if len(args) == 3:
                self.__height = args[2]
            if len(args) == 4:
                self.__x = args[3]
            if len(args) == 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if 'id' == key:
                    self.id = value
                elif 'width' == key:
                    self.__width = value
                elif 'height' == key:
                    self.__height = value
                elif 'x' == key:
                    self.__x = value
                elif 'y' == key:
                    self.__y = value

    def to_dictionary(self):
        """Function that returns a dictionary with all attributes
        of the instance"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
