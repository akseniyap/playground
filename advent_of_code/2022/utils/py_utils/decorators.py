import re
from itertools import groupby
from .constants import NEW_LINE


def strip_newlines(f):
    def wrapper(variation):
        data = f(variation)
        return map(lambda line: line.strip(NEW_LINE), data)
    return wrapper


def to_list(f):
    def wrapper(variation):
        data = f(variation)
        return list(data)
    return wrapper


def to_ints(f):
    def wrapper(variation):
        data = f(variation)
        to_int = lambda element: int(element) if element != "" else ""
        return map(to_int, data)
    return wrapper


def split_to_digits(f):
    def wrapper(variation):
        data = f(variation)
        to_digits = lambda element: list(map(int, element))
        return map(to_digits, data)
    return wrapper


def group_elements(f):
    def wrapper(variation):
        data = f(variation)
        groups = groupby(data, lambda element: element == "")
        return [list(group) for key, group in groups if not key]
    return wrapper


def sum_elements(f):
    def wrapper(variation):
        data = f(variation)
        return map(sum, data)
    return wrapper


def split_lines_by(separator):
    def decorate(f):
        def wrapper(variation):
            data = f(variation)
            return map(lambda line: re.split(separator, line), data)
        return wrapper
    return decorate
