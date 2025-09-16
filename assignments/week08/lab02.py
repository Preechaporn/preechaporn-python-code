""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return self.brand,self.model,self.year
    
class Car(Vehicle):
    def __init__(self,number_of_doors,brand,model,year):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        brand,model,year = super().get_info()
        return brand,model,year,self.number_of_doors

my_car = Car("Toyota", "Corolla", 2020, 4)
print(my_car.get_info())