g = 100  # Global


def f1():
    global g
    g = 200
    a = 1  # Enclosing

    # Local Function
    def f2():
        b = 2  # Local
        nonlocal a
        a = 10
        print(a, b)

    f2()
    print(a)


f1()
