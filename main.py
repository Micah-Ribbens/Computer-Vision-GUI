from GUI.photo_screen import PhotoScreen, NumberStorer
from base.drawable_objects import GameObject
from base.events import Event
from base.utility_classes import HistoryKeeper
from base.velocity_calculator import VelocityCalculator
from gui_components.outline import Outline
from gui_components.text_box import TextBox
from gui_components.text_box_with_title import TextBoxWithTitle
from logic.file_reader import FileReader
from base.important_variables import game_window, background_color
from base.utility_functions import get_next_index, get_prev_index, get_min_number, get_max_number
from base.colors import *
import time
import pygame

file_reader = FileReader("data.txt")

amount_of_tests = file_reader.get_int("number_of_tests")

all_screens = []
correction_screens = []


def data_to_object(data):
    game_objects = []
    for x in range(int(len(data) / 4)):
        game_object = GameObject(data[x * 4], data[x * 4 + 1], data[x * 4 + 3], data[x * 4 + 2], green)
        game_objects.append(game_object)
    return game_objects

for test_number in range(amount_of_tests):
    test_number += 1
    all_objects_data = file_reader.get_number_list(f"test_number{test_number}.all_objects")
    objects_of_interest_data = file_reader.get_number_list(f"test_number{test_number}.objects_of_interest")

    # Short hand fr = FileReader and s = start
    fr = file_reader
    s = f"test_number{test_number}."
    number_storer = NumberStorer(fr.get_double(f"{s}pi_distance"), fr.get_double(f"{s}pi_delta_angle"),
                                 fr.get_double(f"{s}corrected_distance"), fr.get_double(f"{s}corrected_delta_angle"))
    screen = PhotoScreen(data_to_object(all_objects_data), data_to_object(objects_of_interest_data),
                         test_number, amount_of_tests, fr.get_boolean(f"{s}correction_happened"), number_storer)

    if fr.get_boolean(f"{s}correction_happened"):
        correction_screens.append(screen)

    game_window.add_screen(screen)
    all_screens.append(screen)

current_index = 0
right_clicked_last_cycle = False
left_clicked_last_cycle = False
h_clicked_last_cycle = False
current_screens = all_screens
is_displaying_correction_screens = False
while True:
    controls = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    start_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if not left_clicked_last_cycle and controls[pygame.K_LEFT]:
        current_index = get_prev_index(current_index, len(current_screens) - 1)

    if not right_clicked_last_cycle and controls[pygame.K_RIGHT]:
        current_index = get_next_index(current_index, len(current_screens) - 1)

    if not h_clicked_last_cycle and controls[pygame.K_h]:
        is_displaying_correction_screens = not is_displaying_correction_screens
        current_index = 0

    current_screens = correction_screens if is_displaying_correction_screens and len(correction_screens) != 0 else all_screens
    right_clicked_last_cycle = controls[pygame.K_RIGHT]
    left_clicked_last_cycle = controls[pygame.K_LEFT]
    h_clicked_last_cycle = controls[pygame.K_h]
    game_window.display_screen(current_screens[current_index])
    game_window.run()

    VelocityCalculator.time = time.time() - start_time

