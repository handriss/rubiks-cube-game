# coding=utf-8
#  sudo apt-get install python3-tk

from tkinter import *
from cube import RubiksCube

class RubiksCubeGui:

    COLORS = {'G': 'green', 'R': 'red', 'B': 'blue', 'O': 'orange', 'W': 'white', 'Y': 'yellow'}

    def __init__(self, master):

        cube = RubiksCube()
        master.geometry("525x455")
        master.title("Rubik's cube")
        frame = Frame(master)
        frame.place(x=0, y=0, width=500, height=455)
        self.canvas = Canvas(frame, width=500, height=455)
        self.canvas.pack()
        self.state = "flat"

        menu = Menu(master)
        master.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="Select view type", menu=subMenu)
        subMenu.add_command(label="Flat", command=lambda: self.draw_flat(cube))
        subMenu.add_command(label="Stationary 3D", command=lambda: self.draw_stationary_3D(cube))
        # subMenu.add_command(label="Moving 3D", command=cube.move1)
        # subMenu.add_command(label="Draggable 3D", command=cube.move1)

        button_texts = ["||↑", "||↓", "|↑|", "|↓|", "↑||", "↓||", "→--", "←--", "-→-", "-←-", "--→", "--←",
                        "||↰", "||↱", "|↰|", "|↱|", "↰||", "↱||"]

        movements = [
            lambda: self.move_vertical_cw(cube, 2),
            lambda: self.move_vertical_acw(cube, 2),
            lambda: self.move_vertical_cw(cube, 1),
            lambda: self.move_vertical_acw(cube, 1),
            lambda: self.move_vertical_cw(cube, 0),
            lambda: self.move_vertical_acw(cube, 0),
            lambda: self.move_horizontal_cw(cube, 0),
            lambda: self.move_horizontal_acw(cube, 0),
            lambda: self.move_horizontal_cw(cube, 1),
            lambda: self.move_horizontal_acw(cube, 1),
            lambda: self.move_horizontal_cw(cube, 2),
            lambda: self.move_horizontal_acw(cube, 2),
            lambda: self.move_rotate_cw(cube, 2),
            lambda: self.move_rotate_acw(cube, 2),
            lambda: self.move_rotate_cw(cube, 1),
            lambda: self.move_rotate_acw(cube, 1),
            lambda: self.move_rotate_cw(cube, 0),
            lambda: self.move_rotate_acw(cube, 0)
            ]
        i = 0
        for button in button_texts:
            button = Button(master, text=button, command=movements[i])
            button.place(x=425, y=5+i*25, width=100, height=20)
            i += 1

    def move_vertical_cw(self, cube, column):
        cube.move_vertical_cw(column)
        if self.state == "flat":
            self.draw_flat(cube)
        elif self.state == "stationary_3D":
            self.draw_stationary_3D(cube)

    def move_vertical_acw(self, cube, column):
        cube.move_vertical_acw(column)
        if self.state == "flat":
            self.draw_flat(cube)
        elif self.state == "stationary_3D":
            self.draw_stationary_3D(cube)

    def move_horizontal_cw(self, cube, row):
        cube.move_horizontal_cw(row)
        if self.state == "flat":
            self.draw_flat(cube)
        elif self.state == "stationary_3D":
            self.draw_stationary_3D(cube)

    def move_horizontal_acw(self, cube, row):
        cube.move_horizontal_acw(row)
        if self.state == "flat":
            self.draw_flat(cube)
        elif self.state == "stationary_3D":
            self.draw_stationary_3D(cube)

    def move_rotate_cw(self, cube, depth):
        cube.move_rotate_cw(depth)
        if self.state == "flat":
            self.draw_flat(cube)
        elif self.state == "stationary_3D":
            self.draw_stationary_3D(cube)

    def move_rotate_acw(self, cube, depth):
        cube.move_rotate_acw(depth)
        if self.state == "flat":
            self.draw_flat(cube)
        elif self.state == "stationary_3D":
            self.draw_stationary_3D(cube)

    def draw_flat(self, cube):
        self.state = "flat"
        self.canvas.delete('all')

        positions = [[120, 120, cube.front], [120, 20, cube.up], [20, 120, cube.left], [220, 120, cube.right],
                     [120, 220, cube.bottom], [320, 120, cube.rear]]

        for i in range(len(positions)):
            self.draw_one_face(positions[i][0], positions[i][1], positions[i][2])

    def draw_one_face(self, x, y, color):
        coords = [
            [-5, -5, 90, 90, ""],
            [0, 0, 25, 25, self.COLORS.get(color[0][0])],
            [30, 0, 55, 25, self.COLORS.get(color[0][1])],
            [60, 0, 85, 25, self.COLORS.get(color[0][2])],
            [0, 30, 25, 55, self.COLORS.get(color[1][0])],
            [30, 30, 55, 55, self.COLORS.get(color[1][1])],
            [60, 30, 85, 55, self.COLORS.get(color[1][2])],
            [0, 60, 25, 85, self.COLORS.get(color[2][0])],
            [30, 60, 55, 85, self.COLORS.get(color[2][1])],
            [60, 60, 85, 85, self.COLORS.get(color[2][2])]
            ]
        for coord in coords:
            self.canvas.create_rectangle(x+coord[0], y+coord[1], x+coord[2], y+coord[3], fill=coord[4])

    def draw_stationary_3D(self, cube):
        self.state = "stationary_3D"
        self.canvas.delete('all')
        self.draw_3D_cube(130, 140, 30, cube)

    def draw_3D_cube(self, x, y, size, cube):
        coords = [
            [0, 0, "right", self.COLORS.get(cube.front[2][0]), self.COLORS.get(cube.left[2][0])],
            [0, -35, "right", self.COLORS.get(cube.front[1][0]), self.COLORS.get(cube.left[1][0])],
            [0, -70, "right", self.COLORS.get(cube.front[0][0]), self.COLORS.get(cube.left[0][0])],
            [30, -53, "right", self.COLORS.get(cube.front[0][1]), self.COLORS.get(cube.left[0][1])],
            [30, -18, "right", self.COLORS.get(cube.front[1][1]), self.COLORS.get(cube.left[1][1])],
            [30, 17, "right", self.COLORS.get(cube.front[2][1]), self.COLORS.get(cube.left[2][1])],
            [60, -37, "right", self.COLORS.get(cube.front[0][2]), self.COLORS.get(cube.left[0][2])],
            [60, -2, "right", self.COLORS.get(cube.front[1][2]), self.COLORS.get(cube.left[1][2])],
            [60, 33, "right", self.COLORS.get(cube.front[2][2]), self.COLORS.get(cube.left[2][2])],
            [115, -37, "left", self.COLORS.get(cube.right[0][0]), self.COLORS.get(cube.rear[0][0])],
            [115, -2, "left", self.COLORS.get(cube.right[1][0]), self.COLORS.get(cube.rear[1][0])],
            [115, 33, "left", self.COLORS.get(cube.right[2][0]), self.COLORS.get(cube.rear[2][0])],
            [145, -53, "left", self.COLORS.get(cube.right[0][1]), self.COLORS.get(cube.rear[0][1])],
            [145, -18, "left", self.COLORS.get(cube.right[1][1]), self.COLORS.get(cube.rear[1][1])],
            [145, 17, "left", self.COLORS.get(cube.right[2][1]), self.COLORS.get(cube.rear[2][1])],
            [175, -70, "left", self.COLORS.get(cube.right[0][2]), self.COLORS.get(cube.rear[0][2])],
            [175, -35, "left", self.COLORS.get(cube.right[1][2]), self.COLORS.get(cube.rear[1][2])],
            [175, 0, "left",  self.COLORS.get(cube.right[2][2]), self.COLORS.get(cube.rear[2][2])],
            [0, -75, "upper", self.COLORS.get(cube.up[2][0]), self.COLORS.get(cube.bottom[2][0])],
            [30, -58, "upper", self.COLORS.get(cube.up[2][1]), self.COLORS.get(cube.bottom[1][0])],
            [60, -41, "upper", self.COLORS.get(cube.up[2][2]), self.COLORS.get(cube.bottom[0][0])],
            [30, -93, "upper", self.COLORS.get(cube.up[1][0]), self.COLORS.get(cube.bottom[2][1])],
            [60, -76, "upper", self.COLORS.get(cube.up[1][1]), self.COLORS.get(cube.bottom[1][1])],
            [90, -59, "upper", self.COLORS.get(cube.up[1][2]), self.COLORS.get(cube.bottom[0][1])],
            [60, -110, "upper", self.COLORS.get(cube.up[0][0]), self.COLORS.get(cube.bottom[2][2])],
            [90, -93, "upper", self.COLORS.get(cube.up[0][1]), self.COLORS.get(cube.bottom[1][2])],
            [120, -76, "upper", self.COLORS.get(cube.up[0][2]), self.COLORS.get(cube.bottom[0][2])]
        ]
        for coord in coords:
            self.draw_paralelogram(x+coord[0], y+coord[1], size, coord[2], coord[3])
        y += 210
        for coord in coords:
            self.draw_paralelogram(x+coord[0], y+coord[1], size, coord[2], coord[4])

    def draw_paralelogram(self, x, y, size, face, color):
        positions = {'left': -1, 'right': 1, 'upper': 0}
        if positions.get(face) == 0:
            self.canvas.create_polygon(x, y, x+0.87*size, y+0.5*size, x+1.74*size, y, x+0.87*size, y-0.5*size, fill=color)
        else:
            self.canvas.create_polygon(x, y, x, y+size, x+0.87*size*(positions.get(face)), y+1.5*size, x+0.87*size*(positions.get(face)), y+0.5*size, fill=color)

root = Tk()
my_gui = RubiksCubeGui(root)
root.mainloop()
