s = "how do you do"

chars = ""
for c in s:
    if c not in chars:
        print(c, s.count(c))
        chars += c


