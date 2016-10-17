def checkio(words):
    counts = 0
    for w in words.split(' '):
        if counts >= 3:
            break
        elif w.isdigit():
            counts = 0
        else:
            counts += 1

    return counts >= 3


if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
