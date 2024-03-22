def fun():
    print("Hello!")


fun2 = fun
print(id(fun), id(fun2))
a = 100
b = a

print(id(a), id(b))
print(a, b)
fun()
fun2()
