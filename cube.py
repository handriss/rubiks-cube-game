# coding=utf-8


class RubiksCube:

    def __init__(self):
        self.front = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
        self.up = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
        self.right = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]
        self.bottom = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
        self.left = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
        self.rear = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]

        self.facelets = [self.front, self.up, self.right, self.bottom, self.left, self.rear]

    def move_vertical_cw(self, column):
        temp = []
        for element in self.up:
            temp.append(element[column])

        for i in range(3):
            self.up[i][column] = self.front[i][column]
            self.front[i][column] = self.bottom[i][column]
            self.bottom[i][column] = self.rear[i][column]
            self.rear[i][column] = temp[column]

    def move_vertical_acw(self, column):
        temp = []
        for element in self.up:
            temp.append(element[column])
        for i in range(3):
            self.up[i][column] = self.rear[i][column]
            self.rear[i][column] = self.bottom[i][column]
            self.bottom[i][column] = self.front[i][column]
            self.front[i][column] = temp[-1]

    def move_horizontal_cw(self, row):
        temp = []
        for element in list(zip(*self.right)):
            temp.append(element[row])
        for i in range(3):
            self.right[row][i] = self.front[row][i]
            self.front[row][i] = self.left[row][i]
            self.left[row][i] = self.rear[row][i]
            self.rear[row][i] = temp[i]

    def move_horizontal_acw(self, row):
        temp = []
        for element in list(zip(*self.right)):
            temp.append(element[row])
        for i in range(3):
            self.right[row][i] = self.rear[row][i]
            self.rear[row][i] = self.left[row][i]
            self.left[row][i] = self.front[row][i]
            self.front[row][i] = temp[i]

    def move_rotate_cw(self, depth):
        temp = []

        for i in range(3):
            temp.append(self.up[(depth+1)*(-1)][i])

        for i in range(3):
            self.up[(depth+1)*(-1)][i] = self.right[i][depth]
            self.right[i][depth] = self.bottom[depth][i]
            self.bottom[depth][i] = self.left[i][(depth+1)*(-1)]
            self.left[i][(depth+1)*(-1)] = temp[i]

    def move_rotate_acw(self, depth):
        temp = []

        for i in range(3):
            temp.append(self.up[(depth+1)*(-1)][i])

        for i in range(3):
            self.up[(depth+1)*(-1)][i] = self.left[i][(depth+1)*(-1)]
            self.left[i][(depth+1)*(-1)] = self.bottom[depth][i]
            self.bottom[depth][i] = self.right[i][depth]
            self.right[i][depth] = temp[i]
