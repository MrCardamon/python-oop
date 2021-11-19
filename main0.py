"""
class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed= max_speed
        self.mileage= mileage


 

class bus(vehicle):
    pass
"""
#%%


"""
    class Vehicle:
    def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    class Bus(Vehicle):
    def seating_capacity(self, capacity= 50):
        return super().seating_capacity(capacity)


    School_bus = Bus("School Volvo", 180, 12)
    print(School_bus.seating_capacity())   
"""
#%%
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def fare(self):
        return 1.1 * super().fare()

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

print(isinstance(School_bus, Vehicle))
# %%
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print(f"Blu is a {blu.__class__.species}")
print(f"Woo is also a {woo.species}")

