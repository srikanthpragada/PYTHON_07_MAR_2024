names = []
total_length = 0
for n in range(5):
    name = input("Enter name :")
    names.append(name)
    total_length += len(name)

avg_length = total_length // 5

for name in names:
    if len(name) > avg_length:
        print(name)
