num = int(input("Enter number :"))

lfactor = 1
for n in range(2, num // 2 + 1):
    if num % n == 0:
        lfactor = n

print(lfactor)

