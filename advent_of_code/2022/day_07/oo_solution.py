import re

from utils.py_utils.constants import INPUT, ROOT
from utils.py_utils.decorators import strip_newlines, to_list


@to_list
@strip_newlines
def get_data(variation):
    with open(f"inputs/07_{variation}.txt") as f:
        data = f.readlines()
    return data


class ElfFile:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent


    def __repr__(self):
        return f"ElfFile(name='{self.name}' size={self.size}, parent={self.parent.name})"


class ElfDirectory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.content = []


    def __repr__(self):
        return f"ElfDirectory(name='{self.name}' content={len(self.content)}, parent={self.parent.name})"


    @property
    def size(self):
        return sum(map(lambda item: item.size, self.content))


    def add_item(self, item):
        self.content.append(item)


    def find_dir(self, name):
        return list(filter((lambda item: item.name == name), self.content))[0]


    def flatten_directories(self):
        directories = []
        for item in self.content:
            if type(item) == ElfDirectory:
                directories.append(item)
                directories += item.flatten_directories()

        return directories


class ElfFileSystem:
    def __init__(self):
        self.tree = ElfDirectory(ROOT, None)


    @property
    def size(self):
        return self.tree.size


    def flatten_directories(self):
        return self.tree.flatten_directories()


    @classmethod
    def build_tree(cls, data):
        file_system = ElfFileSystem()
        location = file_system.tree

        for line in data[1:]:
            if line.startswith("$ cd"):
                folder_name = re.match("\$ cd (.*)", line)[1]

                if folder_name == "..":
                    location = location.parent
                else:
                    location = location.find_dir(folder_name)

            elif line.startswith("dir"):
                folder_name = re.match("dir (.*)", line)[1]
                elf_dir = ElfFileSystem.mkdir(folder_name, location)
                location.add_item(elf_dir)

            elif re.match("(\d*) (.*)", line):
                size, file_name = line.split(" ")
                elf_file = ElfFileSystem.mkfile(file_name, int(size), location)
                location.add_item(elf_file)

        return file_system


    @classmethod
    def mkfile(cls, name, size, parent):
        return ElfFile(name, size, parent)


    @classmethod
    def mkdir(cls, name, parent):
        return ElfDirectory(name, parent)


def easy(data):
    file_system = ElfFileSystem.build_tree(data)
    directories = file_system.flatten_directories()

    size_limit = 100_000
    filtered = filter(lambda dir: dir.size <= size_limit, directories)
    return sum(map(lambda item: item.size, filtered))


def hard(data):
    file_system = ElfFileSystem.build_tree(data)
    directories = file_system.flatten_directories()

    total_space = 70_000_000
    needed_space = 30_000_000
    free_space = total_space - file_system.size
    need_to_free = needed_space - free_space
    filtered = filter(lambda dir: dir.size >= need_to_free, directories)
    return min(map(lambda item: item.size, filtered))


if __name__ == "__main__":
    data = get_data(INPUT)
    print(easy(data))
    print(hard(data))
