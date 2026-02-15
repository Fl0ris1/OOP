class Student:
    def __init__(self,name,year,):
        self.name=name
        self.year=year

class School(Student):
    def __init__(self, name, year,grade1, grade2, grade3):
        super().__init__(name, year)
        self.grade1=grade1
        self.grade2=grade2
        self.grade3=grade3

    def Calculate(self):
        print(f"The Total Of {self.name} Is: {self.grade1+self.grade2+self.grade3}")
        print(f"The Average Of {self.name} Is: {(self.grade1+self.grade2+self.grade3)/3}")       
        
student1=School(input("Name: "),int(input("Year: ")),int(input("Grade 1: ")),int(input("Grade 2: ")),int(input("Grade 3: ")))
student1.Calculate()