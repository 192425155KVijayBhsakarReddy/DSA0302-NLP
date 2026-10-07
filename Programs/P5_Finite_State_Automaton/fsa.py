def fsa(s):
    state = 0
    path = [state]

    for ch in s:
        if state == 0:
            state = 1 if ch == 'a' else 0
        elif state == 1:
            state = 2 if ch == 'b' else 1 if ch == 'a' else 0
        else:
            state = 1 if ch == 'a' else 0
        path.append(state)

    print("String:", s)
    print("Path:", path)
    print("Accepted" if state == 2 else "Rejected")

strings = ["ab", "aab", "abab", "abc", "baa"]

for s in strings:
    fsa(s)
