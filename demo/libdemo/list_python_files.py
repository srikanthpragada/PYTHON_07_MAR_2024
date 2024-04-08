import os

allfiles = os.walk(r"d:\classroom\mar7")

count = 0
for (dirname, folders, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
            count += 1


print(f"Count = {count}")

