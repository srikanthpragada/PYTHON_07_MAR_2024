from  abc import abstractmethod, ABC
class Doctor(ABC):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def show(self):
        print(f'Name :{self.name}')
        print(f'Dept :{self.dept}')

    @abstractmethod
    def getsalary(self):
        pass

class Resident(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def show(self):
        super().show()
        print(f'Salary :{self.salary}')

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, dept, visits, charge):
        super().__init__(name, dept)
        self.visits = visits
        self.charge = charge

    def show(self):
        super().show()
        print(f'Visits :{self.visits}')
        print(f'Charge :{self.charge}')

    def getsalary(self):
        return self.visits * self.charge


r = Resident("Dr. Jack", "Card", 500000)
r.show()
c = Consultant("Dr. Andy", "Ortho", 10, 1000)
print(c.getsalary())

