from base.dimensions import Dimensions
from base.equations import LineSegment
from gui_components.grid import Grid
from gui_components.outline import Outline
from gui_components.screen import Screen
from gui_components.text_box import TextBox
from gui_components.text_box_with_title import TextBoxWithTitle
from base.utility_functions import *
from base.colors import *
from base.important_variables import *
from base.drawable_objects import GameObject
class PhotoScreen(Screen):
    photo_number_box = None
    amount_of_objects_box = None
    amount_of_objects_of_interest_box = None
    components = []

    def __init__(self, objects, objects_of_interest, screen_number, total_amount_of_screens):
        self.components = []
        self.photo_number_box = TextBox(f"Test Screen Number: {screen_number}/{total_amount_of_screens}", 15, False, blue, white)
        self.amount_of_objects_box = TextBox(f"Amount Of Objects: {len(objects)}", 15, False, brown, white)
        self.amount_of_objects_of_interest_box = TextBox(f"Amount of Objects of Interest: {len(objects_of_interest)}", 15, False, purple, white)
        # TODO figure out the lenght and height of the images
        top_bar_height = screen_height - 480

        grid = Grid(Dimensions(0, 0, screen_length, top_bar_height), None, 1, True)

        self.components += [self.photo_number_box, self.amount_of_objects_box, self.amount_of_objects_of_interest_box]
        grid.turn_into_grid(self.components, None, None)

        for object in objects:
            modified_object = GameObject(object.x_coordinate, object.y_coordinate + top_bar_height, object.height, object.length, object.color)
            self.components.append(modified_object)
        modified_objects_of_interest = []
        for object_of_interest in objects_of_interest:
            modified_object = GameObject(object_of_interest.x_coordinate, object_of_interest.y_coordinate + top_bar_height, object_of_interest.height, object_of_interest.length, object.color)
            modified_objects_of_interest.append(modified_object)
        self.components.append(self.get_outline(modified_objects_of_interest))

    def get_outline(self, objects):
        x_coordinates = []
        y_coordinates = []
        right_edges = []
        bottoms = []

        for object in objects:
            x_coordinates.append(object.x_coordinate)
            y_coordinates.append(object.y_coordinate)
            right_edges.append(object.right_edge)
            bottoms.append(object.y_coordinate + object.height)

        min_x = get_min_number(x_coordinates) - LineSegment.width
        min_y = get_min_number(y_coordinates) - LineSegment.width
        max_right_edge = get_max_number(right_edges) + LineSegment.width
        max_bottom = get_max_number(bottoms) + LineSegment.width

        return Outline(min_x, min_y, max_right_edge - min_x, max_bottom - min_y)

