# Remove duplicate lines

f1 = open("names2.txt", "rt")
unique_lines = []
for line in f1.readlines():
    if not line in unique_lines:
        unique_lines.append(line)

f1.close()

print(unique_lines)
