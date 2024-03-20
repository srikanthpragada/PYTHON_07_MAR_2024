s = "how do you do"

chars = {}
for c in set(s):
    chars[c] = s.count(c)

print(sorted(chars.items()))




