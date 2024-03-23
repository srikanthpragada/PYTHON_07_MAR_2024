def largest_digit(n):
    ldigit = 0
    while n > 0:
        digit = n % 10
        if digit > ldigit:
            ldigit = digit

        n //= 10

    return ldigit


print(largest_digit(19247), largest_digit(1244))
