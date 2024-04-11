from datetime import *
import re

f = open("players.txt", "rt")

players = []
for line in f:
    parts = re.split("[:,;]", line)
    if len(parts) < 2:
        continue

    try:
        dob = datetime.strptime(parts[1].strip(), '%d-%m-%Y')
        td = datetime.today() - dob
        years = td.days // 365

        players.append((parts[0], years))  # Add a tuple with name and age

    except:
        pass

f.close()

# Sort by first element of tuple, which is name
for name, age in sorted(players):
    print(f"{name:20}  {age:2}")

print('-' * 50)

# Sort by second element of tuple, which is age
for name, age in sorted(players, key=lambda p: p[1]):
    print(f"{name:20}  {age:2}")
