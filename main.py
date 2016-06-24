# coding=utf-8

from Tkinter import *
from cube import RubiksCube
# from canvas import Canvas

class RubiksCubeGui:

    COLORS = {'G': 'green', 'R': 'red', 'B': 'blue', 'O': 'orange', 'W': 'white', 'Y': 'yellow'}

    def __init__(self, master):

        cube = RubiksCube()
        master.geometry("525x455")
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

        button1 = Button(master, text="cica||↑", command=lambda: self.move_vertical_cw(cube, 2))
        button2 = Button(master, text="||↓", command=lambda: self.move_vertical_acw(cube, 2))
        button3 = Button(master, text="|↑|", command=lambda: self.move_vertical_cw(cube, 1))
        button4 = Button(master, text="|↓|", command=lambda: self.move_vertical_acw(cube, 1))
        button5 = Button(master, text="↑||", command=lambda: self.move_vertical_cw(cube, 0))
        button6 = Button(master, text="↓||", command=lambda: self.move_vertical_acw(cube, 0))

        button7 = Button(master, text="→--", command=lambda: self.move_horizontal_cw(cube, 0))
        button8 = Button(master, text="←--", command=lambda: self.move_horizontal_acw(cube, 0))
        button9 = Button(master, text="-→-", command=lambda: self.move_horizontal_cw(cube, 1))
        button10 = Button(master, text="-←-", command=lambda: self.move_horizontal_acw(cube, 1))
        button11 = Button(master, text="--→", command=lambda: self.move_horizontal_cw(cube, 2))
        button12 = Button(master, text="--←", command=lambda: self.move_horizontal_acw(cube, 2))

        button13 = Button(master, text="||↰", command=lambda: self.move_rotate_cw(cube, 2))
        button14 = Button(master, text="||↱", command=lambda: self.move_rotate_acw(cube, 2))
        button15 = Button(master, text="|↰|", command=lambda: self.move_rotate_cw(cube, 1))
        button16 = Button(master, text="|↱|", command=lambda: self.move_rotate_acw(cube, 1))
        button17 = Button(master, text="↰||", command=lambda: self.move_rotate_cw(cube, 0))
        button18 = Button(master, text="↱||", command=lambda: self.move_rotate_acw(cube, 0))

        button1.place(x=425, y=5, width=100, height=20)
        button2.place(x=425, y=30, width=100, height=20)
        button3.place(x=425, y=55, width=100, height=20)
        button4.place(x=425, y=80, width=100, height=20)
        button5.place(x=425, y=105, width=100, height=20)
        button6.place(x=425, y=130, width=100, height=20)
        button7.place(x=425, y=155, width=100, height=20)
        button8.place(x=425, y=180, width=100, height=20)
        button9.place(x=425, y=205, width=100, height=20)
        button10.place(x=425, y=230, width=100, height=20)
        button11.place(x=425, y=255, width=100, height=20)
        button12.place(x=425, y=280, width=100, height=20)
        button13.place(x=425, y=305, width=100, height=20)
        button14.place(x=425, y=330, width=100, height=20)
        button15.place(x=425, y=355, width=100, height=20)
        button16.place(x=425, y=380, width=100, height=20)
        button17.place(x=425, y=405, width=100, height=20)
        button18.place(x=425, y=430, width=100, height=20)

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
        self.draw_face(120, 120, cube.front)
        self.draw_face(120, 20, cube.up)
        self.draw_face(20, 120, cube.left)
        self.draw_face(220, 120, cube.right)
        self.draw_face(120, 220, cube.bottom)
        self.draw_face(320, 120, cube.rear)

    def draw_stationary_3D(self, cube):
        self.state = "stationary_3D"
        self.canvas.delete('all')
        self.draw_3D_cube(130, 140, 30, cube)
        self.draw_3D_cube(130, 350, 30, cube)

    def draw_3D_cube(self, x, y, size, cube):
        self.draw_paralelogram(x, y, size, "right", self.COLORS.get(cube.front[2][0])) # 7
        self.draw_paralelogram(x, y - 35, size, "right", self.COLORS.get(cube.front[1][0])) # 4.
        self.draw_paralelogram(x, y - 70, size, "right", self.COLORS.get(cube.front[0][0])) # 1
        self.draw_paralelogram(x + 30, y - 53, size, "right", self.COLORS.get(cube.front[0][1])) # 2
        self.draw_paralelogram(x + 30, y - 18, size, "right", self.COLORS.get(cube.front[1][1])) # 5
        self.draw_paralelogram(x + 30, y + 17, size, "right", self.COLORS.get(cube.front[2][1])) # 8
        self.draw_paralelogram(x + 60, y - 37, size, "right", self.COLORS.get(cube.front[0][2])) # 3
        self.draw_paralelogram(x + 60, y - 2, size, "right", self.COLORS.get(cube.front[1][2])) # 6
        self.draw_paralelogram(x + 60, y + 33, size, "right", self.COLORS.get(cube.front[2][2])) #9

        self.draw_paralelogram(x + 115, y - 37, size, "left", self.COLORS.get(cube.right[0][0])) #1
        self.draw_paralelogram(x + 115, y - 2, size, "left", self.COLORS.get(cube.right[1][0])) # 4
        self.draw_paralelogram(x + 115, y + 33, size, "left", self.COLORS.get(cube.right[2][0])) # 7
        self.draw_paralelogram(x + 145, y - 53, size, "left", self.COLORS.get(cube.right[0][1])) # 2
        self.draw_paralelogram(x + 145, y - 18, size, "left", self.COLORS.get(cube.right[1][1])) #5
        self.draw_paralelogram(x + 145, y + 17, size, "left", self.COLORS.get(cube.right[2][1])) # 8
        self.draw_paralelogram(x + 175, y - 70, size, "left", self.COLORS.get(cube.right[0][2])) # 3
        self.draw_paralelogram(x + 175, y - 35, size, "left", self.COLORS.get(cube.right[1][2])) # 6
        self.draw_paralelogram(x + 175, y, size, "left", self.COLORS.get(cube.right[2][2])) # 9

        self.draw_upper_side(x, y - 75, size, self.COLORS.get(cube.up[2][0])) # 7
        self.draw_upper_side(x + 30, y - 58, size, self.COLORS.get(cube.up[2][1])) # 8
        self.draw_upper_side(x + 60, y - 41, size, self.COLORS.get(cube.up[2][2])) # 9
        self.draw_upper_side(x + 30, y - 93, size, self.COLORS.get(cube.up[1][0])) # 4
        self.draw_upper_side(x + 60, y - 76, size, self.COLORS.get(cube.up[1][1])) #5
        self.draw_upper_side(x + 90, y - 59, size, self.COLORS.get(cube.up[1][2])) # 6
        self.draw_upper_side(x + 60, y - 110, size, self.COLORS.get(cube.up[0][0])) # 1
        self.draw_upper_side(x + 90, y - 93, size, self.COLORS.get(cube.up[0][1])) # 2
        self.draw_upper_side(x + 120, y - 76, size, self.COLORS.get(cube.up[0][2])) # 3

    def draw_paralelogram(self, x, y, size, face, color):
        positions = {'left': -1, 'right': 1}
        self.canvas.create_polygon(x, y, x, y+size, x+0.87*size*(positions.get(face)), y+1.5*size, x+0.87*size*(positions.get(face)), y+0.5*size, fill=color)

    def draw_upper_side(self, x, y, size, color):
        self.canvas.create_polygon(x, y, x+0.87*size, y+0.5*size, x+1.74*size, y, x+0.87*size, y-0.5*size, fill=color)

    def draw_face(self, x, y, color):
        self.middle_face = self.canvas.create_rectangle(x - 5, y - 5, x + 90, y + 90)
        self.middle_face = self.canvas.create_rectangle(x, y, x + 25, y + 25, fill=self.COLORS.get(color[0][0]))
        self.middle_face = self.canvas.create_rectangle(x + 30, y, x + 55, y + 25, fill=self.COLORS.get(color[0][1]))
        self.middle_face = self.canvas.create_rectangle(x + 60, y, x + 85, y + 25, fill=self.COLORS.get(color[0][2]))
        self.middle_face = self.canvas.create_rectangle(x, y + 30, x + 25, y + 55, fill=self.COLORS.get(color[1][0]))
        self.middle_face = self.canvas.create_rectangle(x + 30, y + 30, x + 55, y + 55, fill=self.COLORS.get(color[1][1]))
        self.middle_face = self.canvas.create_rectangle(x + 60, y + 30, x + 85, y + 55, fill=self.COLORS.get(color[1][2]))
        self.middle_face = self.canvas.create_rectangle(x, y + 60, x + 25, y + 85, fill=self.COLORS.get(color[2][0]))
        self.middle_face = self.canvas.create_rectangle(x + 30, y + 60, x + 55, y + 85, fill=self.COLORS.get(color[2][1]))
        self.middle_face = self.canvas.create_rectangle(x + 60, y + 60, x + 85, y + 85, fill=self.COLORS.get(color[2][2]))
#
root = Tk()
my_gui = RubiksCubeGui(root)
root.mainloop()
