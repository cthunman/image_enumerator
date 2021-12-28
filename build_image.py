from typing import Optional, Sequence
from collections import defaultdict

class Grid():
    def __init__(self, height: int, width: int, default_value: int = 0):
        self.height = height
        self.width = width
        self.grid = self.grid(default_value)

    def grid(self, default_value: int = 0) -> Sequence[Sequence]:
        value = default_value
        return [[value for _ in range(self.width)] for _ in range(self.height)]

    def set_value(self, row, column, value) -> None:
        self.grid[row][column] = value

    def apply_layer(self, layer) -> None:
        if self.height != layer.height or self.width != layer.width:
            raise Exception('Applying grid of incorrect size.')
        for i in range(self.height):
            for j in range(self.width):
                if layer.grid[i][j] != 0:
                    self.grid[i][j] = layer.grid[i][j]

    def __str__(self):
        s = ''
        for row in self.grid:
            s += str(row) + '\n'
        return s

class Assembler():
    def __init__(self):
        self.layers: Map = defaultdict(list)

    def get_layer_list(self):
        return sorted([layer for layer in self.layers])

    def get_next_layer(self, layer_number):
        layer_list = self.get_layer_list()
        if layer_number == layer_list[-1]:
            return None
        i = 0
        while i < len(layer_list):
            if layer_number == layer_list[i]:
                return i + 1
        raise Exception("I love off by 1 errors.")

    def add_layer(self, layer_number: int, grid):
        self.layers[layer_number].append(grid)

    def assemble(self) -> Sequence:
        for grid in self.layers[0]:
            return self.assemble_layer(grid, 0)

    def assemble_layer(self, grid, layer_number: int):
        next_layer = self.get_next_layer(layer_number)



    def __str__(self):
        s = ''
        for layer in self.layers:
            s += str(layer) + ' ' + str(len(self.layers[layer])) + '\n'
        return s


def main():
    g = Grid(5, 5, 0)
    g.set_value(0, 0, 1)
    g.set_value(2, 1, 1)
    print("original g")
    print(g)
    f = Grid(5, 5)
    f.set_value(4, 4, 3)
    f.set_value(3, 4, 3)
    print("original f")
    print(f)

    g.apply_layer(f)
    print("f applied to g")
    print(g)

    h = Grid(5, 5)
    h.set_value(0, 0, 5)
    h.set_value(2, 2, 5)
    print("original h")
    print(h)

    print("h applied to g")
    g.apply_layer(h)
    print(g)

    grid_list = [Grid(5, 5, i) for i in range(1, 5)]

    a = Assembler()
    a.add_layer(0, g)
    for g in grid_list:
        a.add_layer(0, g)
    a.add_layer(1, f)
    a.add_layer(3, h)
    print(a)
    print(a.get_layer_list())

main()
