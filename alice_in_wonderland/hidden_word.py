def checkio(text, word):
    def horizontal_word(l):
        position = [0, 0, 0, 0]
        for i, t in enumerate(l):
            if word in t:
                position[0] = i + 1
                position[1] = t.index(word) + 1
                position[2] = i + 1
                position[3] = t.index(word) + len(word)
                return position
        return None

    def vertical_word(l):
        vertical_list = []
        for v in zip(*l):
            vertical_list.append(''.join(v))
        a, b, c, d = horizontal_word(vertical_list)
        return [b, a, d, c]

    texts = [x.lower().replace(' ', '') for x in text.split('\n')]
    m = max([len(x) for x in texts])
    texts = [format(x, str(m)) for x in texts]
    answer = horizontal_word(texts)
    if answer is not None:
        return answer
    return vertical_word(texts)


if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
