HORIZONTAL = ['1', '2', '3', '4', '5', '6', '7', '8']
VERTICAL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


class Pawn(object):
    def __init__(self, position):
        self._h = position[1]
        self._v = position[0]

    def safe(self, pawns):
        if self._is_horizontal_edge():
            return False
        left = self._safe_left(pawns)
        right = self._safe_right(pawns)
        return left or right

    def _is_horizontal_edge(self):
        return self._h == '1'

    def _is_vertical_left_edge(self):
        return self._v == 'a'

    def _is_vertical_right_edge(self):
        return self._v == 'h'

    def _safe_left(self, pawns):
        if self._is_vertical_left_edge():
            return False
        if self._h == '1':
            return False
        v = VERTICAL[VERTICAL.index(self._v) - 1]
        h = HORIZONTAL[HORIZONTAL.index(self._h) - 1]
        return v + h in pawns

    def _safe_right(self, pawns):
        if self._is_vertical_right_edge():
            return False
        if self._h == '1':
            return False
        v = VERTICAL[VERTICAL.index(self._v) + 1]
        h = HORIZONTAL[HORIZONTAL.index(self._h) - 1]
        return v + h in pawns


def safe_pawns(pawns):

    cnt = 0
    for pawn in pawns:
        p = Pawn(pawn)
        if p.safe(pawns):
            cnt += 1

    return cnt


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
