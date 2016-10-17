def find_message(text):
    return ''.join([x for x in text if 64 < ord(x) < 91])


if __name__ == '__main__':
    assert find_message(
        "How are you? Eh, ok. Low or Lower? Ohhh."
    ) == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
