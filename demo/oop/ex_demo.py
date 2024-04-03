s = "0"
try:
    n = int(s)
    print(100 // n)
except ValueError as ex:
    print(ex)
finally:
    print("Finally")

print("Done")
