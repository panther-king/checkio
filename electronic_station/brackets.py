def checkio(expression):
    BRACKETS = {'{': '}',
                '(': ')',
                '[': ']'}
    opens = []

    def get_pair(close):
        pair = None
        for k, v in BRACKETS.items():
            if v == close:
                pair = k
                break
        return pair

    for c in expression:
        if c in BRACKETS.keys():
            opens.append(c)
        elif c in BRACKETS.values():
            if not opens:
                return False
            elif not get_pair(c) == opens[-1]:
                return False
            else:
                opens.pop()

    return True if not opens else False


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
