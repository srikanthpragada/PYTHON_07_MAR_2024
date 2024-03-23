nums = [10, -10, 20, 30, -40]

for n in nums:
    print(abs(n))

for n in map(abs, nums):
    print(n)

