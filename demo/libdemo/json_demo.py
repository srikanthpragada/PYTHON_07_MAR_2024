import json

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


p = Product("iPad Air", 50000)
s = json.dumps(p.__dict__)
print(s)

