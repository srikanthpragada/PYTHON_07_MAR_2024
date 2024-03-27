import sys


def total_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


for arg in sys.argv[1:]:
    num = int(arg)
    total = total_digits(num)
    print(f"{arg} - {total}")
