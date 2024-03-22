def mathop(op, n1, n2):
    print(op(n1, n2))


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


mathop(add, 10, 20)
mathop(mul, 10, 20)
