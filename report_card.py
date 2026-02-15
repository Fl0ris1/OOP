class Student:
    def __init__(self):
        self.name=""
        self.year=""
        

class Report(Student):
    def __init__(self):
        super().__init__()
        self.m1=0
        self.m2=0
        self.m3=0
        self.total=0
        self.average=0
        self.grade=""
        
    def inputs(self):
        self.name=input("Name: ")
        self.year=input("Year: ")
        self.m1=int(input("Mark For Maths: "))
        self.m2=int(input("Mark For Science: "))
        self.m3=int(input("Mark For Physics: "))
        

    def calculations(self):
        self.total=self.m1+self.m2+self.m3
        self.average=(self.m1+self.m2+self.m3)/3
        
    def showDetails(self):
        print("The Details Of The Student Are:")
        print(f"Name: {self.name}")
        print(f"Year: {self.year}")
        print(f"Average: {self.average}")
        
        if self.average == 100:
            print("Grade: A+")
        elif self.average < 100 and self.average>=90:
            print("Grade: A")
            
        elif self.average < 90 and self.average>=80:
            print("Grade: B")
            
        elif self.average < 80 and self.average>=70:
            print("Grade: C") 
            
        elif self.average < 70 and self.average>=60:
            print("Grade: D") 
            
        elif self.average < 60:
            print("Grade: F") 
        

Floris=Report()
Floris.inputs()
Floris.calculations()
Floris.showDetails()
        