class Course:
    # Constructor
    def __init__(self, title, fee=5000):
        # Object attributes
        self.title = title
        self.fee = fee

    def __str__(self):
        return f"{self.title} - {self.fee}"

    def __repr__(self):
        return f"{self.title} - {self.fee}"


courses = [Course("Java SE", 17500),
           Course("Python", 15000),
           Course("DS", 20000)]

for c in sorted(courses, key=lambda c: c.fee):
    print(c)
