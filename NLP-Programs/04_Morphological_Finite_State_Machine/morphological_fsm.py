def plural(word):
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"
    else:
        return word + "s"

words = ["cat", "dog", "box", "bus", "watch"]

for word in words:
    print(word, "->", plural(word))
