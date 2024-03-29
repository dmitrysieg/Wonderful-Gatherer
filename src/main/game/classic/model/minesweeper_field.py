import random
import wx


class MSCell:
    def __init__(self):
        self.mines = 0
        self.around = 0
        self.revealed = False


class MSField:
    def __init__(self, game_view, width, height):
        self.game_view = game_view
        self.width = width
        self.height = height
        self.field = []
        self.mines = []
        self.mines_left = None
        self.initialize()

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

    @staticmethod
    def define_mine(x, y):
        if random.randint(0, 99) < 10:
            return 1
        else:
            return 0

    def is_mine(self, x, y):
        return self.field[y][x].mines > 0

    def reveal(self, x, y):
        self.field[y][x].revealed = True
        around = self.get_around(x, y)
        if around > 0:
            self.game_view.show_amount(x, y, around)
            self.game_view.after_reveal_cell(x, y)
        else:
            self.reveal_around(x, y)
            self.game_view.after_reveal_cell(x, y)

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

    def reveal_around(self, x, y):
        visited = [[False for i in range(self.width)] for j in range(self.height)]
        visited[y][x] = True
        stack = self.get_next(visited, x, y)
        while len(stack) > 0:

            front = []
            for (_x, _y) in stack:

                visited[_y][_x] = True
                cell = self.field[_y][_x]

                if not cell.revealed:
                    cell.revealed = True
                    self.game_view.after_reveal_cell(_x, _y)

                if cell.around > 0:
                    self.game_view.show_amount(_x, _y, cell.around)
                else:
                    front.extend(self.get_next(visited, _x, _y))
            stack = front


