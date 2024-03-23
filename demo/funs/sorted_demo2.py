names = ['Joe', 'andy', 'bill', 'Kevin']

nums = ['100', '5', '200', '35']

for n in sorted(names, key=str.upper):
    print(n, end=' ')

for n in sorted(nums, key=int):
    print(n, end=' ')
