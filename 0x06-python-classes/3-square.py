#!/usr/bin/python3


class Square:
    """private instance
    Attributes:
        _size(int): side measure
        """

    def __init__(self, size=0):
        """
        Args:
            size(int): side measure1.
        """
        if type(size) is int:
            """If size is not integer jump to last else*"""
            if size < 0:
                """If size is integer execute"""
                raise ValueError('size must be >= 0')
            else:
                self._size = size
        else:
            raise ValueError('size must be an integer')

    def area(self):
        """
        Finding area of Square
        :return: Area
        """
        return self._size ** 2
