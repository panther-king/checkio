def checkio(n, m):
    def bin_format(num):
        return format(num, 'b').zfill(20)

    bin_n = bin_format(n)
    bin_m = bin_format(m)

    return sum(x != y for x, y in zip(bin_n, bin_m))

if __name__ == '__main__':
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
