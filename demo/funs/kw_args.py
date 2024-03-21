def show(**details):
    print(type(details))
    print(details)


def showall(*args, **kwargs):
    pass


showall(10, 20, x=10, y=20)

show(a=10, b=20)
show(name="Python", version=3.12)
