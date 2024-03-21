# positional-only args
def wish(message, name, /):
    print(f"{message} {name}")


wish("Hi", "Larry")  # positional

