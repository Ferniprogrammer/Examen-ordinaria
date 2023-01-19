import random

def create_grid(n, chances=1):
    grid = []
    for i in range(n):
        line = []
        for j in range(n):
            rand = random.randint(0, 1)
            line.append(rand)
        grid.append(line)
    return grid
def print_grid(grid):
    for line in grid:
        print(line)
def valid_grid(grid):
    if grid == []:
        return False

    for line in grid:
        if sum(line) == 0:
            return False

    tgrid = transpose_grid(grid)
    for line in tgrid:
        if sum(line) == 0:
            return False

    return True
def transpose_grid(grid):
    return [[row[i] for row in grid] for i in range(len(grid))]
if __name__ == '__main__':
    n = 5
    grid = []

    while not valid_grid(grid):
        grid = create_grid(n)
    print_grid(grid)
