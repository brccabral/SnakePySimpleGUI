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

window = sg.Window("Snake", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
