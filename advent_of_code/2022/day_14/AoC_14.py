import os


AIR = "."
ROCK = "#"
SAND = "o"

data = []
with open(os.getcwd() + "/day_14/sample.txt") as file:
    for line in file:
        coordinates = list(map(lambda x: x.strip(), line.split("->")))
        data.append([[int(x) for x in el.split(",")] for el in coordinates])

min_cols = min([x[0] for item in data for x in item])
min_rows = min([x[1] for item in data for x in item])
max_cols = max([x[0] for item in data for x in item])
max_rows = max([x[1] for item in data for x in item])
grid = [[AIR] * (max_cols - min_cols + 1) for _ in range(max_rows + 1)]

increment = lambda x, y: 1 if x < y else -1
for line in data:
    transitions = list(zip(line, line[1:]))
    for transition in transitions:
        start, end = transition
        x1, y1 = start
        x2, y2 = end

        if x1 == x2:
            step = increment(y1, y2)
            for j in range(y1, y2 + step, step):
                grid[j][x1-min_cols] = ROCK
        elif y1 == y2:
            step = increment(x1, x2)
            for i in range(x1, x2 + step, step):
                grid[y1][i-min_cols] = ROCK
        else:
            grid[x1][y1] = ROCK

grid[0][500-min_cols] = "+"

down_pos = lambda x, y: grid[x+1][y]
left_diagonal = lambda x, y: grid[x+1][y-1]
right_diagonal = lambda x, y: grid[x+1][y+1]
out_of_range = lambda x, y: x < 0 or min_rows > y or y > max_rows

def waterfall(floor=False):
    extended_grid = []
    if floor:
        grid.append((max_cols - min_cols +1) * [AIR])
        grid.append((max_cols - min_cols +1) * [ROCK])
        for line in grid:
            extended_grid.append(5 * [AIR] + line + 5 * [AIR])


    sand_units = 0

    down_pos = lambda x, y: extended_grid[x+1][y]
    left_diagonal = lambda x, y: extended_grid[x+1][y-1]
    right_diagonal = lambda x, y: extended_grid[x+1][y+1]

    while True:
        new_unit = (0, 500-min_cols)
        can_move = True
        while can_move:
            try:
                moves = {
                    (new_unit[0]+1, new_unit[1]): down_pos(*new_unit),
                    (new_unit[0]+1, new_unit[1]-1): left_diagonal(*new_unit),
                    (new_unit[0]+1, new_unit[1]+1): right_diagonal(*new_unit)
                }
            except IndexError:
                return sand_units


            for coordinates, element in moves.items():
                if element == AIR:
                    new_unit = coordinates
                    break

            if sorted(set(list(moves.values()))) == ["#"] or sorted(set(list(moves.values()))) == ["o"] or sorted(set(list(moves.values()))) == ["#", "o"]:
                can_move = False
                extended_grid[new_unit[0]][new_unit[1]] = SAND
                sand_units += 1


def part_one():
    return waterfall()


def part_two():
    return waterfall(True)



def main():
    # part_one()
    part_two()
    # test_input_file = "test_input.dat"
    # test_input = parse(test_input_file)
    # assert part1(test_input) == 13

    # input_file = "input.dat"
    # input_parsed = parse(input_file)
    # print(part1(input_parsed))

    # assert part2(test_input) == 140
    # print(part2(input_parsed))


if __name__ == "__main__":
    main()
