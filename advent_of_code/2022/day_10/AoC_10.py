import os

data = []
with open(os.getcwd() + "/AoC/2022/day_10/input.txt") as file:
    for line in file:
        data.append(line.strip())

def part_one(data):
    signal_strengths = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
    cycles = 0
    register = 1

    for line in data:
        if "addx" in line:
            count = int(line.split("addx ")[1])
            for _ in range(2):
                cycles += 1
                if cycles in [20, 60, 100, 140, 180, 220]:
                    signal_strengths[cycles] = register * cycles

            register += count
        elif "noop" in line:
            cycles += 1
            if cycles in [20, 60, 100, 140, 180, 220]:
                signal_strengths[cycles] = register * cycles

    return sum(list(signal_strengths.values()))


def part_two(data):
    crt = ""
    cycles = 0
    sprite = []
    register = 1

    for line in data:
        sprite = [register - 1, register, register + 1]
        if "addx" in line:
            count = int(line.split("addx ")[1])
            for _ in range(2):
                cycles += 1
                if len(crt) % 40 in sprite:
                    crt += "#"
                else:
                    crt += "."
            register += count

        elif "noop" in line:
            cycles += 1
            if len(crt) % 40 in sprite:
                crt += "#"
            else:
                crt += "."

    return [crt[0:40], crt[40:80], crt[80:120], crt[120:160], crt[160:200], crt[200:240]]


print(part_one(data))
print(part_two(data))

if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
