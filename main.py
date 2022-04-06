import PySimpleGUI as sg

FIELD_SIZE = 400

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
    event, values = window.read()
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

window.close()
