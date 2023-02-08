import re
from itertools import groupby
from .constants import NEW_LINE


def strip_newlines():
    def decorated(f):
        def inner(variation):
            data = f(variation)
            return map(lambda line: line.strip(NEW_LINE), data)
        return inner
    return decorated


def to_list():
    def decorated(f):
        def inner(variation):
            data = f(variation)
            return list(data)
        return inner
    return decorated


def to_ints():
    def decorated(f):
        def inner(variation):
            data = f(variation)
            to_int = lambda element: int(element) if element != "" else ""
            return map(to_int, data)
        return inner
    return decorated


def group_elements():
    def decorated(f):
        def inner(variation):
            data = f(variation)
            groups = groupby(data, lambda element: element == "")
            return [list(group) for key, group in groups if not key]
        return inner
    return decorated


def sum_elements():
    def decorated(f):
        def inner(variation):
            data = f(variation)
            return map(sum, data)
        return inner
    return decorated


def split_lines_by(separator):
    def decorated(f):
        def inner(variation):
            data = f(variation)
            return map(lambda line: re.split(separator, line), data)
        return inner
    return decorated
