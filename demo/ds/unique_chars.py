s = "how do you do"

chars = []
for c in s:
    if c not in chars:
        chars.append(c)


print("".join(chars))