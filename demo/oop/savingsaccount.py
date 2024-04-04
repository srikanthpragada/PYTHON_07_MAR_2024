class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Invalid Transaction Amount : {self.amount}"


class SavingsAccount:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)

        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError('Insufficient Balance')

    @property
    def currentbalance(self):
        return self.balance

    def show(self):
        print(self.acno)
        print(self.ahname)
        print(self.balance)


s1 = SavingsAccount(1, "Ben", 100000)
s1.deposit(-1000)
s1.withdraw(-200000)

s2 = SavingsAccount(2, "Cathy")
s1.deposit(10000)
s2.deposit(50000)
print(s2.currentbalance)
s1.show()
