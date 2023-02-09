import os


def contains_operation(str):
    operations = {"+", "-", "*", "/"}
    return any(map(lambda operator: operator in str, operations))


data = {}
with open(os.getcwd() + '/day_21/sample.txt') as file:
    for line in file:
        key, value = line.strip().split(": ")
        if not contains_operation(line):
            data[key] = int(value)
        else:
            data[key] = value.split(" ")


def solve(key):
    while True:
        value = data[key]

        if isinstance(value, int):
            return value
        else:
            lhs, operator, rhs = value
            if isinstance(lhs, int) and isinstance(rhs, int):
                value = list(map(str, value))
                data[key] = int(eval("".join(value)))
            elif isinstance(lhs, str):
                res = solve(lhs)
                data[key] = [res, operator, rhs]
            elif isinstance(rhs, str):
                res = solve(rhs)
                data[key] = [lhs, operator, res]


def part_one():
    res = solve("root")
    return res


def part_two():
    return data


# print(part_one())
# print(part_two())


if __name__ == "__main__":
    # pass
    print(part_one())
    # print(part_two())
