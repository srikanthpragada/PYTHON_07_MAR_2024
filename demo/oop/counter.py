class Counter:
    def __init__(self, value=0):
        #object attributes
        self.init_value = value
        self.value = value

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def getvalue(self):
        return self.value

    def reset(self):
        self.value = self.init_value


c1 = Counter(100)
c1.inc()   # call method
#c1.value = 50
print(c1.getvalue())
c1.reset()
c1.dec()
c1.dec()
print(c1.getvalue())
