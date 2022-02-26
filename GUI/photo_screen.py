from base.dimensions import Dimensions
from gui_components.grid import Grid
from turtle import Screen, back
from gui_components.text_box_with_title import TextBoxWithTitle
from base.colors import *
from base.important_variables import *
from base.drawable_objects import GameObject
class PhotoScreen(Screen):
    photo_number_box = None
    amount_of_objects_box = None
    amount_of_objects_of_interest_box = None
    components = []

    def __init__(self, objects, objects_of_interest, screen_number, total_amount_of_screens):
        self.photo_number_box = TextBoxWithTitle(15, f"{screen_number}/{total_amount_of_screens}", "Screen Number", blue, background_color)
        self.amount_of_objects_box = TextBoxWithTitle(15, len(objects), "Amount of Objects", green, background_color)
        self.amount_of_objects_of_interest_box = TextBoxWithTitle(15, len(objects_of_interest), "Amount of Objects of Interest", purple, background_color)
        # TODO figure out the lenght and height of the images
        top_bar_height = 100

        grid = Grid(Dimensions(0, 0, screen_length, top_bar_height))

        self.components += [self.photo_number_box, self.amount_of_objects_box, self.amount_of_objects_of_interest_box]
        grid.turn_into_grid(self.components, None, None)

        for object in objects:
            modified_object = GameObject(object.x_coordinate, object.y_coordinate + top_bar_height, object.height, object.length)
            self.components.append(modified_object)

