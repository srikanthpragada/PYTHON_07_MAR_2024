
names = ["Java", "JavaScript", "Python", "C#", 'SQL']

f = open("names.txt", "wt")


for n in names:
    f.write(n + "\n")

f.close()



