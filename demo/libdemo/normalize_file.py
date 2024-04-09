import re

with open("test.txt", "rt") as f:
    contents = f.read()

contents = re.sub(' +', ' ', contents)
contents = re.sub(r'\n+', '\n', contents)

with open("test.txt", "wt") as f:
    f.write(contents)
