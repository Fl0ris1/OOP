#base
class Vehicle:
    def __init__(self,brand):
        self.brand=brand

    def showBrand(self):
        print(f"Brand: {self.brand}")

#derived
class Bike(Vehicle):
    def __init__(self, brand,type ):
        super().__init__(brand)
        self.type=type

    def showType(self):
        print(f"Bike Type: {self.type}")

#further derived
class EBike(Bike):
    def __init__(self, brand, type, batteryCapacity):
        super().__init__(brand, type)
        self.batteryCapacity=batteryCapacity

    def showCapacity(self):
        print(f"E-bike Battery Capacity: {self.batteryCapacity}")


bike1=EBike("Eleglide", "Mountain Bike", "15.6Ah")

bike1.showBrand()
bike1.showType()
bike1.showCapacity()
 