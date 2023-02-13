import re
from functools import reduce

from utils.py_utils.constants import INPUT, ROOT
from utils.py_utils.decorators import strip_newlines, to_list


@to_list
@strip_newlines
def get_data(variation):
    with open(f"inputs/07_{variation}.txt") as f:
        data = f.readlines()
    return data


file_system = {ROOT: {}}
def build_file_tree(data):
    def parent_dir(file_system, *path):
        return reduce((lambda dir, key: dir.get(key)), path, file_system)

    current_path = []
    list_items = False

    for line in data:
        if line.startswith("$ cd"):
            list_items = False
            folder = re.match("\$ cd (.*)", line)[1]

            if folder == "..":
                current_path.pop()
            else:
                current_path.append(folder)

        elif line.startswith("$ ls"):
            list_items = True

        elif list_items:
            parent = parent_dir(file_system, *current_path)

            if line.startswith("dir"):
                folder = re.match("dir (.*)", line)[1]
                parent.update({folder: {}})
            elif re.match("(\d*) (.*)", line):
                size, file_name = line.split(" ")
                parent.update({file_name: int(size)})


dir_sizes = {}
def dir_size(file_system, path):
    size = 0

    for item, content in file_system.items():
        if type(content) == dict:
            path.append(item)
            size += dir_size(file_system[item], path)
        else:
            size += content

    dir_sizes["/".join(path)] = size
    path.pop()
    return size


def easy(data):
    build_file_tree(data)
    dir_size(file_system[ROOT], [ROOT])

    size_limit = 100_000

    return sum([
        dir_size
        for dir_size in dir_sizes.values()
        if dir_size <= size_limit
    ])


def hard(data):
    build_file_tree(data)
    dir_size(file_system[ROOT], [ROOT])

    total_space = 70_000_000
    needed_space = 30_000_000
    free_space = total_space - dir_sizes[ROOT]
    need_to_free = needed_space - free_space

    return min([
        dir_size
        for dir_size in dir_sizes.values()
        if dir_size >= need_to_free
    ])


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
