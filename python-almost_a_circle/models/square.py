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

    def update(self, *args, **kwargs):
        """Function that updates attributes of an instance"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if 'id' == key:
                    self.id = value
                elif 'size' == key:
                    self.width = value
                    self.height = value
                elif 'x' == key:
                    self.x = value
                elif 'y' == key:
                    self.y = value

    def to_dictionary(self):
        """Function that returns a dictionary with all attributes
        of the instance"""
        return {'id': self.id, 'x': self.x, 'size': self.width,
                'y': self.y}
