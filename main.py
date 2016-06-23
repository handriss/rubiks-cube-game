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
        frame.place(x=0, y=0, width=500, height=325)
        self.canvas = Canvas(frame, width=500, height=325)
        self.canvas.pack()

        menu = Menu(master)
        master.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="Select view type", menu=subMenu)
        subMenu.add_command(label="Flat", command=lambda: self.draw_flat(cube))
        subMenu.add_command(label="Stationary 3D", command=lambda: self.draw_stationary_3D(cube))
        # subMenu.add_command(label="Moving 3D", command=cube.move1)
        # subMenu.add_command(label="Draggable 3D", command=cube.move1)

        button1 = Button(master, text="||↑", command=lambda: self.move_vertical_cw(cube, 2))
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
        self.draw_flat(cube)

    def move_vertical_acw(self, cube, column):
        cube.move_vertical_acw(column)
        self.draw_flat(cube)

    def move_horizontal_cw(self, cube, row):
        cube.move_horizontal_cw(row)
        self.draw_flat(cube)

    def move_horizontal_acw(self, cube, row):
        cube.move_horizontal_acw(row)
        self.draw_flat(cube)

    def move_rotate_cw(self, cube, depth):
        cube.move_rotate_cw(depth)
        self.draw_flat(cube)

    def move_rotate_acw(self, cube, depth):
        cube.move_rotate_acw(depth)
        self.draw_flat(cube)

    def draw_flat(self, cube):
        self.canvas.delete('all')
        self.draw_face(120, 120, cube.front)
        self.draw_face(120, 20, cube.up)
        self.draw_face(20, 120, cube.left)
        self.draw_face(220, 120, cube.right)
        self.draw_face(120, 220, cube.bottom)
        self.draw_face(320, 120, cube.rear)

    def draw_stationary_3D(self, cube):
        self.canvas.delete('all')
        # self.canvas.create_polygon(50, 50, 50, 100, 100, 100, 200, 200)
        # self.canvas.create_polygon(200, 200, 100, 200, 50, 120, 50, 170, fill="green")
        self.canvas.create_line(200, 200, 200, 100)
        self.canvas.create_line(200, 100, 300, 80)


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
