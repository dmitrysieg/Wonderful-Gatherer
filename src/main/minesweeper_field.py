import random
import wx


class MSCell:
    def __init__(self):
        self.mines = 0
        self.around = 0
        self.revealed = False


class MSField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = []
        self.mines = []
        self.mines_left = None

    def initialize(self):

        # create random mines
        for j in range(0, self.height):
            self.field.append([])
            for i in range(0, self.width):
                cell = MSCell()
                cell.mines = MSField.define_mine(i, j)
                if cell.mines > 0:
                    self.mines.append((i, j))

                self.field[j].append(cell)

        self.mines_left = len(self.mines)

        # calc numbers
        for j in range(0, self.height):
            for i in range(0, self.width):
                self.field[i][j].around = self.get_around(j, i)

        return self

    @staticmethod
    def define_mine(x, y):
        if random.randint(0, 99) < 10:
            return 1
        else:
            return 0

    def is_mine(self, x, y):
        return self.field[y][x].mines > 0

    def get_around(self, x, y):
        sum = 0
        if x > 0:
            sum += self.field[y][x - 1].mines
            if y > 0:
                sum += self.field[y - 1][x - 1].mines
            if y < self.height - 1:
                sum += self.field[y + 1][x - 1].mines
        if y > 0:
            sum += self.field[y - 1][x].mines
        if y < self.height - 1:
            sum += self.field[y + 1][x].mines
        if x < self.width - 1:
            sum += self.field[y][x + 1].mines
            if y > 0:
                sum += self.field[y - 1][x + 1].mines
            if y < self.height - 1:
                sum += self.field[y + 1][x + 1].mines
        return sum

    def visit(self, acc, visited, x, y):
        if not visited[y][x]:
            acc.append((x, y))
            visited[y][x] = True

    def get_next(self, visited, x, y):
        next = []
        if x > 0:
            self.visit(next, visited, x - 1, y)
            if y > 0:
                self.visit(next, visited, x - 1, y - 1)
            if y < self.height - 1:
                self.visit(next, visited, x - 1, y + 1)
        if y > 0:
            self.visit(next, visited, x, y - 1)
        if y < self.height - 1:
            self.visit(next, visited, x, y + 1)
        if x < self.width - 1:
            self.visit(next, visited, x + 1, y)
            if y > 0:
                self.visit(next, visited, x + 1, y - 1)
            if y < self.height - 1:
                self.visit(next, visited, x + 1, y + 1)
        return next

    def reveal_around(self, game_panel, x, y):
        visited = [[False for i in range(self.width)] for j in range(self.height)]
        visited[y][x] = True
        stack = self.get_next(visited, x, y)
        while len(stack) > 0:

            front = []
            for (_x, _y) in stack:

                visited[_y][_x] = True
                cell = self.field[_y][_x]

                if not cell.revealed:
                    game_panel.buttons[_y][_x].Destroy()
                    cell.revealed = True

                if cell.around > 0:
                    wx.StaticText(game_panel, pos=(_x * 20, _y * 20), label=str(cell.around))
                else:
                    front.extend(self.get_next(visited, _x, _y))
            stack = front


