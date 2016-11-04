def checkio(data):
    def to_morse(l):
        return ''.join(['.' if x == '0' else '-' for x in l])

    h, m, s = [int(x) for x in data.split(':')]
    h, m, s = '{0:02d}:{1:02d}:{2:02d}'.format(h, m, s).split(':')

    h1 = '{:02b}'.format(int(h[0]))
    h2 = '{:04b}'.format(int(h[1]))

    m1 = '{:03b}'.format(int(m[0]))
    m2 = '{:04b}'.format(int(m[1]))

    s1 = '{:03b}'.format(int(s[0]))
    s2 = '{:04b}'.format(int(s[1]))

    return '{} {} : {} {} : {} {}'.format(to_morse(h1),
                                          to_morse(h2),
                                          to_morse(m1),
                                          to_morse(m2),
                                          to_morse(s1),
                                          to_morse(s2))


if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
