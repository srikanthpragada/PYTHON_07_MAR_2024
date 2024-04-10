from datetime import *
import re

f = open("players.txt", "rt")

for line in f:
    parts = re.split("[:,;]", line)
    if len(parts) < 2:
        continue

    try:
        dob = datetime.strptime(parts[1].strip(), '%d-%m-%Y')
        td = datetime.today() - dob
        years = td.days // 365

        print(f"{parts[0]:20}  {years:2}")
    except:
        pass

f.close()
