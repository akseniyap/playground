def split_data(pattern):
    def decorated(f):
        def inner(variation):
            data = f(variation)
            return data.split(pattern)
        return inner
    return decorated


def split_elements_by(separator):
    def decorated(f):
        def inner(variation):
            data = f(variation)
            return map(lambda el: el.split(separator), data)
        return inner
    return decorated


def to_ints():
    def decorated(f):
        def inner(variation):
            data = f(variation)
            to_ints = lambda line: [int(el) for el in line]
            return map(to_ints, data)
        return inner
    return decorated
