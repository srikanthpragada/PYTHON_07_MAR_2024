class SavingsAccount:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    @property
    def currentbalance(self):
        return self.balance

    def show(self):
        print(self.acno)
        print(self.ahname)
        print(self.balance)


s1 = SavingsAccount(1, "Ben", 100000)
s2 = SavingsAccount(2, "Cathy")
s1.deposit(10000)
s2.deposit(50000)
print(s2.currentbalance)
s1.show()
