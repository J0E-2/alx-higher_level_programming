#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """define object attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """object instantiation using the init method"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves current width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the current width size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves current height size"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height size"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter if width or
        height is not 0"""
        if self.__width == 0 or self.__height == 0:
            return (0)

        else:
            return (2 * (self.__width + self.__height))

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")

    def __str__(self):
        """prints the rectangle with the character # """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ("")

        else:
            for i in range(self.__height):
                string += str(self.print_symbol) * self.__width

                if i != self.__height - 1:
                    string += "\n"

            return string

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            a = rect_1.area()
            b = rect_2.area()
            if a > b:
                return rect_1
            elif rect_1.area() == rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
