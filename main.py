import random
import time
from typing import Tuple
import PySimpleGUI as sg


def convert_position_to_pixels(cell: Tuple[int, int]):
    top_left = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
    bottom_right = top_left[0] + CELL_SIZE, top_left[1] + CELL_SIZE
    return top_left, bottom_right


def place_apple():
    apple_pos = random.randint(0, CELL_NUM - 1), random.randint(0, CELL_NUM - 1)
    while apple_pos in snake_body:
        apple_pos = random.randint(0, CELL_NUM - 1), random.randint(0, CELL_NUM - 1)
    return apple_pos


# game constants
FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE / CELL_NUM
DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, 1), "down": (0, -1)}

# snake
snake_body = [(4, 4), (3, 4), (2, 4)]
direction = DIRECTIONS["up"]

# apple
apple_pos = place_apple()

sg.theme("Green")

field = sg.Graph(
    canvas_size=(FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left=(0, 0),
    graph_top_right=(FIELD_SIZE, FIELD_SIZE),
    background_color="black",
)
layout = [[field]]

window = sg.Window("Snake", layout, return_keyboard_events=True)

start_time = time.time()
while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break

    if event == "Left:113":  # in tutorial video this was Left:37
        direction = DIRECTIONS["left"]
    elif event == "Up:111":
        direction = DIRECTIONS["up"]
    elif event == "Right:114":
        direction = DIRECTIONS["right"]
    elif event == "Down:116":
        direction = DIRECTIONS["down"]

    time_size_start = time.time() - start_time
    if time_size_start >= 0.5:
        start_time = time.time()

        # snake update
        new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
        snake_body.insert(0, new_head)
        if new_head == apple_pos:
            apple_pos = place_apple()
        else:
            snake_body.pop()

        if (
            not 0 <= new_head[0] <= CELL_NUM - 1
            or not 0 <= new_head[1] <= CELL_NUM - 1
            or new_head in snake_body[1:]
        ):
            break

        field.DrawRectangle((0, 0), (FIELD_SIZE, FIELD_SIZE), "black")

        top_left, bottom_right = convert_position_to_pixels(apple_pos)
        field.draw_rectangle(top_left, bottom_right, "red")

        # draw snake
        for index, part in enumerate(snake_body):
            top_left, bottom_right = convert_position_to_pixels(part)
            color = "yellow" if index == 0 else "green"
            field.draw_rectangle(top_left, bottom_right, color)

window.close()
