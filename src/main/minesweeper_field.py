import random


class WGField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = []

    def initialize(self):
        for j in range(0, self.height):
            self.field.append([])
            for i in range(0, self.width):
                self.field[j].append(random.randint(0, 1))
        return self

    def get(self, x, y):
        return self.field[y][x]
