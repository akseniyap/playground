import os
import functools


data = []
with open(os.getcwd() + '/day_13/input.txt') as file:
    for line in file:
        line = line.strip()
        if line != "":
            data.append(eval(line))
data = [data[i:i + 2] for i in range(0, len(data), 2)]


def ordered(left, right):
    is_ordered = None
    left_iter = iter(left)
    right_iter = iter(right)

    while is_ordered == None:
        a = next(left_iter, "")
        b = next(right_iter, "")

        if a == "" and b == "":
            return is_ordered
        if a == "" and b != "":
            is_ordered = 1
        if a != "" and b == "":
            is_ordered = -1

        if type(a) == int and type(b) == int:
            if a < b:
                is_ordered = 1
            elif a == b:
                continue
            else:
                is_ordered = -1
        elif type(a) == int and type(b) == list:
            a = [a]
        elif type(a) == list and type(b) == int:
            b = [b]

        if type(a) == list and type(b) == list:
            res = ordered(a, b)
            if res != None:
                return res

    return is_ordered

# print(ordered([1,1,3,1,1], [1,1,5,1,1]))
# print(ordered([[1],[2,3,4]], [[1],4]))
# print(ordered([9], [[8,7,6]]))
# print(ordered([[4,4],4,4], [[4,4],4,4,4]))
# print(ordered([7,7,7,7], [7,7,7]))
# print(ordered([], [3]))
# print(ordered([[[]]], [[]]))
# print(ordered([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))


def part_one():
    count = 0

    for i in range(1, len(data)+1):
        left, right = data[i-1]
        if ordered(left, right):
            count += i

    return count


def part_two():
    pack1 = [[2]]
    pack2 = [[6]]

    entities = [pack1, pack2]
    for a, b, in data:
        entities.append(a)
        entities.append(b)

    sorted_entries = sorted(entities, key=functools.cmp_to_key(ordered), reverse=True)
    res = (sorted_entries.index(pack1)+1) * (sorted_entries.index(pack2)+1)
    return res


# print(part_one())
# print(part_two())


if __name__ == "__main__":
    pass
    # print(part_one())
    print(part_two())
