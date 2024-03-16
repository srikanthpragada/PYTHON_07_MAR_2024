names = ['Larry', 'Mark', "Elon", 'Bill']
ages = [40, 35, 43]

for n, a in zip(names, ages, strict=True):
    print(f"{n:15} {a:2}")
