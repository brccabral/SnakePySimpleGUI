import PySimpleGUI as sg

# game constants
FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE / CELL_NUM

# apple
apple_pos = (2, 4)

sg.theme("Green")

field = sg.Graph(
    canvas_size=(FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left=(0, 0),
    graph_top_right=(FIELD_SIZE, FIELD_SIZE),
    background_color="black",
)
layout = [[field]]

window = sg.Window("Snake", layout, return_keyboard_events=True)

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break

    if event == "Left:113":  # in tutorial video this was Left:37
        print("left")
    if event == "Up:111":
        print("up")
    if event == "Right:114":
        print("right")
    if event == "Down:116":
        print("down")

    top_left = apple_pos[0] * CELL_SIZE, apple_pos[1] * CELL_SIZE
    bottom_right = top_left[0] + CELL_SIZE, top_left[1] + CELL_SIZE

    field.draw_rectangle(top_left, bottom_right, "red")

window.close()
