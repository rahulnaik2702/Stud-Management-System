from person import Persons
from database import data,save

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