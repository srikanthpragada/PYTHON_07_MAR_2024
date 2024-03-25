l = [1, 22, 34, 45, 56, 89]

evens = filter(lambda n: n % 2 == 0, l)

for n in evens:
    print(n)
