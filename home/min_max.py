def target(arguments):
    if len(arguments) == 1:
        return arguments[0]
    else:
        return arguments


def max(*args, **kwargs):
    _args = target(args)
    if 'key' not in kwargs:
        return sorted(_args)[-1]

    values = [kwargs['key'](x) for x in _args]
    idx = 0
    for i, v in enumerate(values):
        if v > values[idx]:
            idx = i
    return _args[idx]


def min(*args, **kwargs):
    _args = target(args)
    if 'key' not in kwargs:
        return sorted(_args)[0]

    values = [kwargs['key'](x) for x in _args]
    idx = 0
    for i, v in enumerate(values):
        if v < values[idx]:
            idx = i
    return _args[idx]


if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
