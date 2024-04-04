total = 0
i = 1
while i <= 5:
    try:
        num = int(input("Enter number :"))
        total += num
        i += 1
    except:
        print("Invalid Number")

print(total)
