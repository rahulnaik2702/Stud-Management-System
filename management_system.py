from student import Student
from teacher import Teacher

stud = Student()
tech = Teacher()


print("WELCOME TO WEBSITE")
print("PRESS 1 FOR STUDENT REGISTERATION")
print("PRESS 2 FOR TEACHER REGISTERATION")
print("PRESS 3 FOR ADDING GRADES")
print("PRESS 4 FOR STUDENT DETAILS") 
print("PRESS 5 FOR TEACHER DETAILS")

options = int(input("enter the option number:"))


if options == 1:
    stud.register()
elif options == 2:
    tech.register()
elif options == 3:
    stud.grade()
elif options == 4:
    stud.show_details()
elif options == 5:
    tech.show_details()