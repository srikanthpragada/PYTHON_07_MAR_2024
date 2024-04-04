
def numbers():
    print("First")
    yield 1
    print("Second")
    yield 2


n = numbers()
print(type(n))
print(next(n))
print(next(n))






