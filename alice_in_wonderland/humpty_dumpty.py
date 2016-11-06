import math


def eccentricity(h, w):
    if h > w:
        l = h
        s = w
    else:
        l = w
        s = h
    return math.sqrt(1 - ((s / l) ** 2))


def rounded(l):
    return [round(x, 2) for x in l]


def checkio(height, width):
    h = height / 2
    w = width / 2
    if h == w:
        v = (4 / 3) * math.pi * (h ** 3)
        s = 4 * math.pi * (h ** 2)
        return rounded([v, s])
    else:
        v = (4 / 3) * math.pi * ((w ** 2) * h)
        e = eccentricity(height, width)
        if h > w:
            s = 2 * math.pi * ((w ** 2) + ((w * h) * math.asin(e) / e))
        else:
            s = 2 * math.pi * ((w ** 2) + ((h ** 2) * math.atanh(e) / e))
        return rounded([v, s])


if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
