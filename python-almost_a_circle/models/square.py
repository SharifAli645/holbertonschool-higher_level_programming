#!/usr/bin/python3
"""
Module of
classes that
define geometric
figures
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that defines
    a geometric figure
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor of Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding the str method"""
        return f"""[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}"""

    @property
    def size(self):
        """Getter function of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter function of size"""
        self.width = value
        self.height = value
