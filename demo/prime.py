num = int(input("Enter number :"))

prime = True
for n in range(2, num // 2 + 1):
    if num % n == 0:
        prime = False
        break

if prime:
    print("Prime")
else:
    print("Not prime")






