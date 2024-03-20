
chars = set()
for n in range(5):
    name = input("Enter your name :")
    chars = chars | set(name)

print(sorted(chars))

