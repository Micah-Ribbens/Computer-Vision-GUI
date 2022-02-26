from GUI.photo_screen import PhotoScreen
from base.velocity_calculator import VelocityCalculator
from logic.file_reader import FileReader
from base.important_variables import game_window
from base.utility_functions import get_next_index, get_prev_index
import time
import pygame

file_reader = FileReader("data.txt")

amount_of_tests = file_reader.get_int("number_of_tests")


screens = []

for test_number in amount_of_tests:
    all_objects = file_reader.get_number_list(f"test_number{test_number}.all_objects")
    objects_of_interest = file_reader.get_number_list(f"test_number{test_number}.objects_of_interest")
    screen = PhotoScreen(all_objects, objects_of_interest, test_number, amount_of_tests)
    game_window.add_screen(screen)

current_index = 0

while True:
    controls = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    start_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    game_window.run()

    if controls[pygame.K_LEFT]:
        current_index = get_prev_index(current_index)
    
    if controls[pygame.K_RIGHT]:
        current_index = get_next_index(current_index, len(screens) - 1)
    
    game_window.display_screen(screens[current_index])
    game_window.run()


    VelocityCalculator.time = time.time() - start_time
