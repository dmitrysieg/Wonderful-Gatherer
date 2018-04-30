import random
import wx


class WGCell:
    def __init__(self):
        self.mines = 0
        self.around = 0
        self.revealed = False


class WGField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = []

    def initialize(self):

        # create random mines
        for j in range(0, self.height):
            self.field.append([])
            for i in range(0, self.width):
                cell = WGCell()
                if random.randint(0, 99) < 10:
                    cell.mines = 1

                self.field[j].append(cell)

        # calc numbers
        for j in range(0, self.height):
            for i in range(0, self.width):
                self.field[i][j].around = self.getAround(j, i)

        return self

    def isMine(self, x, y):
        return self.field[y][x].mines > 0

    def getAround(self, x, y):
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

    def getNext(self, visited, x, y):
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

    def RevealAround(self, v_game_panel, x, y):
        visited = [[False for i in range(self.width)] for j in range(self.height)]
        visited[y][x] = True
        stack = self.getNext(visited, x, y)
        while len(stack) > 0:

            front = []
            for (_x, _y) in stack:

                visited[_y][_x] = True
                cell = self.field[_y][_x]

                if not cell.revealed:
                    v_game_panel.buttons[_y][_x].Destroy()
                    cell.revealed = True

                if cell.around > 0:
                    wx.StaticText(v_game_panel, pos=(_x * 20, _y * 20), label=str(cell.around))
                else:
                    front.extend(self.getNext(visited, _x, _y))
            stack = front


