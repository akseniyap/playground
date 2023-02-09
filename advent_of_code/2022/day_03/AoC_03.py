data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip())

def part_one(data):
    result = 0
    errors = []

    for line in data:
        first, second = line[:len(line)//2], line[len(line)//2:]
        errors.append([char for char in first if char in second][0])

    for letter in errors:
        if letter.isupper():
            result += ord(letter) - 38
        else:
            result += ord(letter) - 96

    return result


print(part_one(data))


def part_two(data):
    groups = [data[x:x+3] for x in range(0, len(data), 3)]
    badges = []
    result = 0

    for group in groups:
        badge = [char for char in group[0] if char in group[1] and char in group[2]][0]
        badges.append(badge)


    for letter in badges:
        if letter.isupper():
            result += ord(letter) - 38
        else:
            result += ord(letter) - 96

    return result

print(part_two(data))
