filename = input("Enter filename :")

f = open(filename, "rt")

contents = f.read()

chars = len(contents)
lines = contents.count('\n')
words = contents.count(' ') + lines

print(f"Chars : {chars}")
print(f"Word  : {words}")
print(f"Lines : {lines}")
