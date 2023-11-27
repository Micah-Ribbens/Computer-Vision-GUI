from base.equations import LineSegment, Point
from gui_components.component import Component
from base.colors import *


class Outline(Component):
    def run(self):
        pass

    lines = []
    is_runnable = False

    def __init__(self, x_coordinate, y_coordinate, length, height):
        super().__init__(x_coordinate, y_coordinate, length, height)
        self.lines = [
            LineSegment(Point(x_coordinate, y_coordinate), Point(x_coordinate + length, y_coordinate)),
            LineSegment(Point(x_coordinate, y_coordinate), Point(x_coordinate, y_coordinate + height)),
            LineSegment(Point(x_coordinate, y_coordinate + height), Point(x_coordinate + length, y_coordinate + height)),
            LineSegment(Point(x_coordinate + length, y_coordinate), Point(x_coordinate + length, y_coordinate + height))
        ]

    def render(self):
        for line in self.lines:
            line.color = red
            line.render()



