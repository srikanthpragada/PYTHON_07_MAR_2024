data = "90-88-b-76-45"

nums = data.split('-')

total = 0
for n in nums:
    total += int(n)

print(total)
