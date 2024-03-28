class Course:
    # Constructor
    def __init__(self, title, fee=5000, duration=36):
        # Object attributes
        self.title = title
        self.fee = fee
        self.duration = duration
        self.taxrate = 12

    def net_fee(self):
        return self.fee + (self.fee * self.taxrate // 100)


# Create an object
c1 = Course("AWS", 5000, 24)
c1.fee = 10000
print(c1.net_fee())
print(c1.title)

c2 = Course("Java SE", duration=30)
