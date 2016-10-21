def checkio(year):
    from datetime import date

    days = filter(lambda d: d.weekday() == 4,
                  [date(year, m, 13) for m in range(1, 13)])

    return len(list(days))


if __name__ == '__main__':
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
