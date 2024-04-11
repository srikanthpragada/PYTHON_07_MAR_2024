from datetime import *
f = open("tasks.txt", "rt")

for line in f:
    parts = line.split(",")
    if len(parts) < 3:
        continue

    try:
        stdate = datetime.strptime(parts[1].strip(), '%d-%m-%Y')
        enddate = datetime.strptime(parts[2].strip(), '%d-%m-%Y')
        days = (enddate - stdate).days
        print(f"{parts[0]:50}  {days:3}")
    except:
        pass

f.close()
