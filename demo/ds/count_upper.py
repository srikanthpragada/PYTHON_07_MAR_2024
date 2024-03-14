
name = input("Enter string :")

count = 0

for c in name:
    if c.isupper():
        count += 1

print(count)
