class Student:
    def __init__(self,name,age,year):
        self.name=name
        self.age=age
        self.year=year

    def showInfo(self):
        print("The Details Of The Student Are:")
        print(f"Name: {self.name}\nAge: {self.age}\nYear: {self.year}")

class School(Student):
    def __init__(self, name, age, year,ID,teacher):
        super().__init__(name, age, year)
        self.ID=ID
        self.teacher=teacher

    def showDetails(self):
        print("The Details Of The Student Are:")
        print(f"ID: {self.ID}\nTeacher: {self.teacher}")

    
student1=School("Floris",14,3,401874,"Tolman")
student1.showInfo()
student1.showDetails()        