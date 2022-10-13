#!/usr/bin/python3
"""Defines MagicClass"""
import math


class MagicClass:
    """Circle"""

    def __init__(self, radius=0):
        """Initialize Magic Class
        Args:
            radius(int) = radius of the circle
        """
        self._radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._radius = radius

    def area(self):
        """Area of the circle"""
        return (self._radius ** 2) * math.pi

    def circumference(self):
        """Circumference of the circle"""
        return 2 * math.pi * self._radius
