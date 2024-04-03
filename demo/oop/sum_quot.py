total = 0
for i in range(5):
    try:
        num = int(input("Enter number :"))
        total += 100 // num
    except ValueError:
        print("Invalid Input. Enter Valid Number!")
    except ZeroDivisionError:
        print("Zero is not valid!")

print(total)
