from person import Persons
from database import data,save


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