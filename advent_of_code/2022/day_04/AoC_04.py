data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip().split(','))

def part_one(data):
    count = 0
    for first, second in data:
        a, b = first.split('-')
        c, d = second.split('-')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if (a <= c and b >= d) or (c <= a and d >= b):
            count += 1

    return count


print(part_one(data))


def part_two(data):
    count = 0
    for first, second in data:
        a, b = first.split('-')
        c, d = second.split('-')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if (a <= c and b >= d) or (c <= a and d >= b) or (c <= a <= d) or (a <= c <= b):
            count += 1

    return count

print(part_two(data))
