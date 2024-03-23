def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


nums = [10, 11, 24, 47, 89]

for n in filter(isprime, nums):
    print(n)
