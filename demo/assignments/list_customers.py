data = ["Mark,39393933", "Jason,3929222",
        "Andy,39399222", "39393933",
        "Robers,39113322,34", 'Mark,1939393933']

customers = {}

for e in data:
    parts = e.split(",")
    if len(parts) >= 2:
        customers[parts[0]] = parts[1]


for name, mobile in sorted(customers.items()):
    print(f"{name:20} {mobile}")