import json
from abc import ABC,abstractmethod
from pathlib import Path

database = "school_data.json"
data = {"students": [],"teachers" : []}

if Path(database).exists():
    with open(database,'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(database,"w") as f:
        json.dump(data,f,indent=4)


class Persons(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod  
    def validate_number(number):
        if len(number)==10:
            return True
        else:
            return False


class Student(Persons):

    def get_roles(self):
        return "student"
    
    def register(self):
        name = input("Enter The Name:")
        age = input("Enter The Age:")
        number = input("Enter The Phone Number:")
        roll_no = input("Enter The Roll-NO:")

        while not Persons.validate_number(number):
            print("invalid mobile number")
            return
        
        for i in data['students']:
            if i['roll_no'] == roll_no:
                print("student already exists")
                return
            
  
        data['students'].append({
            "name" : name,
            "age" : age,
            "phone_no" : number,
            "roll_no" : roll_no,
            "grades" : {}
        })
        save()
        print(f"Student Name {name} Is Been Registed!")

    def show_details(self):
        roll_no = input("Enter The Student Roll-no:")
        for s in data['students']:
            if s['roll_no'] == roll_no:
                grades = s['grades']
                avg = sum(grades.values())/len(grades) if grades else 0
                
                print(f"\n Name = {s['name']}")
                print(f" Roll no = {s['roll_no']}")
                print(f" Phone no = {s['phone_no']}")
                print(f" Grade = {grades}")
                print(f" Average = {avg}")
                return

    def grade(self):
        roll_no = input("Enter The Roll-no:")
        subject = input("Enter The Subject:")
        Marks = float(input("Enter the MARKS:"))

        for i in data['students']:
            if i['roll_no']==roll_no:
                i['grades'][subject] = Marks
                save()
                print("Grade Added!!")
                return





class Teacher(Persons):

    def get_roles(self):
        return "teacher"
    
    def register(self):
        name = input("Enter The Name:")
        age = input("Enter The Age:")
        number = input("Enter The Phone Number:")
        subject = input("Enter The Subject:")
        teach_id = input("Enter The ID Number:")

        while not Persons.validate_number(number):
            print("invalid mobile number")
            return

        for i in data['teachers']:
                if i['teach_id'] == teach_id:
                    print("student already exists")
                    return
                
    
        data['teachers'].append({
            "name" : name,
            "age" : age,
            "phone_no" : number,
            "subject" : subject,
            "teach_id" : teach_id
        })
        save()
        print(f"Teacher name {name} Is Been Registed!")

    def show_details(self):
        teach_id = input("Enter The Teacher id_no:")
        for t in data['teachers']:
            if t['teach_id'] == teach_id:
                print(f"\n Name = {t['name']}")
                print(f" Subject = {t['subject']}")
                print(f" Phone no = {t['phone_no']}")
                return
            print("Teacher Not found!!")


stud = Student()
tech = Teacher()



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





print("WELCOME TO WEBSITE")
