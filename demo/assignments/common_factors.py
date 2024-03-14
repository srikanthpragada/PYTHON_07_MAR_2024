
n1 = 10
n2 = 20

# find out smallest of two numbers
sn = n1 if n1 < n2 else n2

for i in range(2, sn//2 + 1):
    if n1 % i == 0 and n2 % i == 0:
        print(i)


