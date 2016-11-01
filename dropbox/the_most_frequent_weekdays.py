def most_frequent_days(year):
    import datetime

    days_count = [0, 0, 0, 0, 0, 0, 0]
    weekdays = ['Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                'Sunday']

    d = datetime.timedelta(days=1)
    start = datetime.date(year, 1, 1)
    limit = datetime.date(year, 12, 31)
    while True:
        weekday = start.weekday()
        days_count[weekday] += 1
        if start == limit:
            break
        start = start + d

    frequent = max(days_count)
    frequents = []
    for i, cnt in enumerate(days_count):
        if frequent == cnt:
            frequents.append(weekdays[i])

    return frequents


if __name__ == '__main__':
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
