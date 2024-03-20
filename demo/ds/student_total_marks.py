allmarks = [(5, 90), (1, 50), (2, 65), (3, 90),
            (1, 69), (3, 45), (3, 80),
            (2, 70), (4, 55)]

students = {}
for rollno, marks in allmarks:
    if rollno in students:
        students[rollno] = students[rollno] + marks
    else:
        students[rollno] = marks

for rollno, total in sorted(students.items()):
    print(f"{rollno:3}  {total:3}")
