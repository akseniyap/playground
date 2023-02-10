from utils.py_utils.constants import INPUT


def get_data(variation):
    with open(f"inputs/06_{variation}.txt") as f:
        data = f.read()
    return data


def sliding_window(data, n):
    for i in range(len(data)-n):
        marker = data[i:i+n]

        if len(set(marker)) == n:
            return i + n


def easy(data):
    return sliding_window(data, 4)


def hard(data):
    return sliding_window(data, 14)


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
