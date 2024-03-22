def iseven(n):
    return n % 2 == 0


l = [1, 22, 34, 45, 56, 89]

evens = filter(iseven, l)

for n in evens:
    print(n)
