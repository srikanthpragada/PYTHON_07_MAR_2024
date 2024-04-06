filename = "test.txt"
with open(filename, "rt") as f:
    lines = f.readlines()

with open(filename, "wt") as f:
    for line in lines:
        if len(line.strip()) > 0:
            f.write(line)
