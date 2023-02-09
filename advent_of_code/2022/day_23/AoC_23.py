import os


ROUNDS = 10

data = []
grid = []
with open(os.getcwd() + "/AoC/2022/day_23/input.txt") as file:
    for line in file:
        data.append([*line.strip()])


for line in data:
    grid.append(["."] * 80 + line + ["."] * 80)

grid = ([
    ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0])]) + grid + ([["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]) + ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0]), ["."] * len(grid[0])
])


# movements:
# (x-1,y-1), (x-1,y), (x-1,y+1)
# (x,  y-1), (x,  y), (x,  y+1)
# (x+1,y-1), (x+1,y), (x+1,y+1)
can_go_north = lambda x, y: grid[x-1][y-1] == "." and grid[x-1][y] == "." and grid[x-1][y+1] == "."
can_go_south = lambda x, y: grid[x+1][y-1] == "." and grid[x+1][y] == "." and grid[x+1][y+1] == "."
can_go_west = lambda x, y: grid[x-1][y-1] == "." and grid[x][y-1] == "." and grid[x+1][y-1] == "."
can_go_east = lambda x, y: grid[x-1][y+1] == "." and grid[x][y+1] == "." and grid[x+1][y+1] == "."
no_adjacents = lambda x, y: all([can_go_north(x, y), can_go_south(x, y), can_go_west(x, y), can_go_east(x, y)])
move_north = lambda x, y: (x-1, y)
move_south = lambda x, y: (x+1, y)
move_west = lambda x, y: (x, y-1)
move_east = lambda x, y: (x, y+1)

def part_one():
    direction_priorities = ["north", "south", "west", "east"]
    for _ in range(ROUNDS):
        propossals = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "#":
                    for direction in direction_priorities:
                        if no_adjacents(i, j):
                            break
                        if eval(f"can_go_{direction}(i, j)"):
                            propossals[(i, j)] = eval(f"move_{direction}(i, j)")
                            break

        direction_priorities = direction_priorities[1:] + [direction_priorities[0]]

        moves = list(propossals.values())
        for key, value in propossals.items():
            if moves.count(value) > 1:
                propossals[key] = None

        for key, value in propossals.items():
            if value:
                x1, y1 = key
                grid[x1][y1] = "."
                x2, y2 = value
                grid[x2][y2] = "#"

    while list(set(grid[0])) == ["."]:
        grid.pop(0)

    while list(set(grid[-1])) == ["."]:
        grid.pop(-1)

    while list(set([grid[i][0] for i in range(len(grid))])) == ["."]:
        for line in grid:
            line.pop(0)

    while list(set([grid[i][-1] for i in range(len(grid))])) == ["."]:
        for line in grid:
            line.pop(-1)

    elves = sum([line.count("#") for line in grid])
    res = len(grid) * len(grid[0]) - elves
    return res

def part_two():
    direction_priorities = ["north", "south", "west", "east"]
    counter = 1
    while True:
        last_grid = [row[:] for row in grid]
        propossals = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "#":
                    for direction in direction_priorities:
                        if no_adjacents(i, j):
                            break
                        if eval(f"can_go_{direction}(i, j)"):
                            propossals[(i, j)] = eval(f"move_{direction}(i, j)")
                            break

        direction_priorities = direction_priorities[1:] + [direction_priorities[0]]

        moves = list(propossals.values())
        for key, value in propossals.items():
            if moves.count(value) > 1:
                propossals[key] = None

        for key, value in propossals.items():
            if value:
                x1, y1 = key
                grid[x1][y1] = "."
                x2, y2 = value
                grid[x2][y2] = "#"

        if last_grid == grid:
            break
        else:
            print(counter)
            counter += 1

    return counter


# print(part_one())
# print(part_two())


def main():
    # part_one()
    part_two()


if __name__ == "__main__":
    main()
