strings = ["hello", "hello123", "12345", "hello world", ""]

for s in strings:
    print("String:", s)
    print("Length:", len(s))
    print("Alphabetic:", s.isalpha())
    print("Digit:", s.isdigit())
    print("Alphanumeric:", s.isalnum())
    print("Empty:", s == "")
    print()
