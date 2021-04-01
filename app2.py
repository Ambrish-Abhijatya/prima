from classes import Student
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
student3 = Student("Oscar", "Accounting", 3.5, False)
student4 = Student("Phyllis", "Buisness", 3.8, True)

print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.is_on_probation)
print(student2.gpa)
print(student3.on_honour_roll())
print(student4.on_honour_roll())