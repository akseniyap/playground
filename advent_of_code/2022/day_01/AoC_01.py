data = []

with open('input.txt') as file:
    for line in file:
        if line == '\n':
            data.append('break')
        else:
            data.append(line.strip())


def split_list(lst, sep):
    return [i.split() for i in ' '.join(lst).split(sep)]


def part_one(data):
    data = split_list(data, 'break')
    data = [list(map(int, row)) for row in data]
    result = [sum(row) for row in data]
    return max(result)

print(part_one(data))


def part_two(data):
    data = split_list(data, 'break')
    data = [list(map(int, row)) for row in data]
    result = [sum(row) for row in data]
    return sum(sorted(result)[-3:])

print(part_two(data))
