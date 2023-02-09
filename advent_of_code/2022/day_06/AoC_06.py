data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip())

def part_one(data):
    input_string = data[0]
    for i in range(len(input_string) - 4):
        substring = input_string[i:i+4]

        if len(set(substring)) == 4:
            return i + 4

# print(part_one(data))


def part_two(data):
    input_string = data[0]
    for i in range(len(input_string) - 14):
        substring = input_string[i:i+14]

        if len(set(substring)) == 14:
            return i + 14

print(part_two(data))
