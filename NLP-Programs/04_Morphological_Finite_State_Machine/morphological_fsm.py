def plural(word):
    state = 0

    for ch in word:
        if ch == 's':
            state = 1
        else:
            state = 0

    if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return word + "es"
    else:
        return word + "s"

words = ["cat", "dog", "box", "bus", "watch"]

for word in words:
    print(word, "->", plural(word))
