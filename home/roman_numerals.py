def checkio(data):
    romans_table = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
                    ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                    ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                    ['M', 'MM', 'MMM']]
    romans = []

    for i, s in enumerate(str(data)[::-1]):
        if s == '0':
            continue
        idx = int(s) - 1
        romans.append(romans_table[i][idx])

    return ''.join(romans[::-1])


if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
