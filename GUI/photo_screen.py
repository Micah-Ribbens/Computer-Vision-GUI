import pygame

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


class NumberStorer:
    """Stores the data for the start and end distance and delta angle. End being what the vision rio got and
    start being what pi got"""

    start_distance = 0
    end_distance = 0

    start_delta_angle = 0
    end_delta_angle = 0

    def __init__(self, start_distance, start_delta_angle, end_distance, end_delta_angle):
        """Initializes the object"""

        self.start_distance = start_distance
        self.end_distance = end_distance
        self.start_delta_angle = start_delta_angle
        self.end_delta_angle = end_delta_angle


class PhotoScreen(Screen):
    photo_number_box = None
    amount_of_objects_box = None
    amount_of_objects_of_interest_box = None
    components = []
    file_name = ""
    top_bar_height = screen_height - 480
    screen_number = 0

    def __init__(self, objects, objects_of_interest, screen_number, total_amount_of_screens, correction_happened, number_storer: NumberStorer):
        self.screen_number = screen_number
        self.photo_number_box = TextBox(f"Test Screen Number: {screen_number}/{total_amount_of_screens}", 15, False, black, white)
        self.amount_of_objects_box = TextBox(f"Amount Of Objects: {len(objects)}", 15, False, brown, white)
        self.amount_of_objects_of_interest_box = TextBox(f"Amount of Objects of Interest: {len(objects_of_interest)}", 15, False, purple, white)
        start_distance_box = TextBox(f"Distance From Pi: {number_storer.start_distance}", 15, False, red, white)
        start_delta_angle_box = TextBox(f"Delta Angle From Pi: {number_storer.start_delta_angle}", 15, False, red, white)
        end_distance_angle_box = TextBox(f"Distance From Rio: {number_storer.end_distance}", 15, False, dark_green, white)
        end_delta_angle_box = TextBox(f"Delta Angle From Rio: {number_storer.end_delta_angle}", 15, False, dark_green, white)
        correction_happened_box = TextBox(f"Correction Happened: {correction_happened}", 15, False, magenta, white)

        grid = Grid(Dimensions(0, 0, screen_length, self.top_bar_height), None, 2, True)

        self.components = [self.photo_number_box, self.amount_of_objects_box, self.amount_of_objects_of_interest_box, start_delta_angle_box, start_distance_box, end_delta_angle_box, end_distance_angle_box, correction_happened_box]
        grid.turn_into_grid(self.components, None, None)

        modified_objects_of_interest = []
        for object_of_interest in objects_of_interest:
            modified_object = GameObject(object_of_interest.x_coordinate, object_of_interest.y_coordinate + self.top_bar_height, object_of_interest.height, object_of_interest.length)
            modified_objects_of_interest.append(modified_object)

        self.components.append(self.get_outline(modified_objects_of_interest))

    def get_outline(self, objects):
        x_coordinates = []
        y_coordinates = []
        right_edges = []
        bottoms = []

        if len(objects) == 0:
            return Outline(0, 0, 0, 0)

        for object in objects:
            x_coordinates.append(object.x_coordinate)
            y_coordinates.append(object.y_coordinate)
            right_edges.append(object.right_edge)
            bottoms.append(object.y_coordinate + object.height)

        buffer = 10
        min_x = get_min_number(x_coordinates) - buffer
        min_y = get_min_number(y_coordinates) - buffer + self.top_bar_height
        max_right_edge = get_max_number(right_edges) + buffer
        max_bottom = get_max_number(bottoms) + buffer + self.top_bar_height

        return Outline(min_x, min_y + 70, max_right_edge - min_x, max_bottom - min_y - 80)

    def render(self):
        raw_image = pygame.transform.scale(pygame.image.load(f"images/raw_image_{self.screen_number - 1}.ppm"), (640, screen_height - self.top_bar_height))
        game_window.get_window().blit(raw_image, (0, self.top_bar_height))
        annotated_image = pygame.transform.scale(pygame.image.load(f"images/annotated_image_{self.screen_number - 1}.pnm"), (640, screen_height - self.top_bar_height))
        game_window.get_window().blit(annotated_image, (640, self.top_bar_height))
        for component in self.components:
            component.render()



