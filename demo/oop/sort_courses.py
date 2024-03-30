class Course:
    # Constructor
    def __init__(self, title, fee=5000):
        # Object attributes
        self.title = title
        self.fee = fee

    def __lt__(self, other):
        return self.fee < other.fee

    def __str__(self):
        return f"{self.title} - {self.fee}"

    def __repr__(self):
        return f"{self.title} - {self.fee}"


courses = [Course("Java SE", 17500),
           Course("Python", 15000),
           Course("DS", 20000)]

courses.sort()
print(courses)
for c in courses:
    print(c)
