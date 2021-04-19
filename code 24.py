def make_word():
    words = ""
    for ch in "spam":
        words += ch
        yield words


print(list(make_word()))
