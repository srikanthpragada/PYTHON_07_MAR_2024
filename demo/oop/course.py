class Course:
    # static attribute or class attribute
    taxrate = 12

    # Constructor
    def __init__(self, title, fee=5000, duration=36):
        # Object attributes
        self.title = title
        self.fee = fee
        self.duration = duration

    def net_fee(self):
        return self.fee + (self.fee * Course.taxrate // 100)

    @staticmethod
    def gettaxrate():
        return Course.taxrate


# Create an object
c1 = Course("AWS", 5000, 24)
print(c1.net_fee())
print(Course.gettaxrate())

c2 = Course("Java SE", duration=30)
