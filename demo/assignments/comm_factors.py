def common_factors(*nums):
    smallest = min(nums)
    factors = []
    for n in range(2, smallest // 2 + 1):
        # check whether n is a factor for all nums
        for v in nums:
            if v % n != 0:
                break
        else:
            factors.append(n)

    print(factors)


common_factors(12, 24, 40)
common_factors(10, 27)

