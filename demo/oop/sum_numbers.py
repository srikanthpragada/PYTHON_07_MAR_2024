total = 0
for i in range(5):
    try:
        num = int(input("Enter number :"))
        total += num
    except:
        print("Invalid Number")

print(total)
