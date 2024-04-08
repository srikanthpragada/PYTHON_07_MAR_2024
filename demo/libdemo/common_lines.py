# Print common lines between two files

f1 = open("names.txt", "rt")
f2 = open("names2.txt", "rt")

# Remove \n from each line
first_lines = list(map(lambda l : l.strip(), f1.readlines()))

comm_lines = []
for line in f2.readlines():
    line = line.strip()
    if line == "":
        continue

    if line in first_lines:
        if line not in comm_lines:
            comm_lines.append(line)

f1.close()
f2.close()

print(comm_lines)
