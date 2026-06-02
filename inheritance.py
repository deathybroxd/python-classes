class Vehicle:
    def __init__(self, type, fuel_type):
        self.type = type
        self.fuel_type = fuel_type
    
    def run(self):
        return f"{self.type} is running!"

class Car(Vehicle): # inheritance
    def __init__(self, type, fuel_type, gas_amount):
        # two ways, the typical non-pythonic way:
        # self.type = type
        # self.gas_amount = gas_amount

        # the recommended way with .super():
        super().__init__(type, fuel_type) # this is like using an intialization list in c++
        self.gas_amount = gas_amount
    
    def display_gas(self):
        return f"{self.gas_amount} gallons of gas"

class Bulldozer(Vehicle):
    def __init__(self, type, fuel_type, can_bulldoze):
        super().__init__(type, fuel_type)
        self.can_bulldoze = can_bulldoze

    def bulldoze(self):
        if not self.can_bulldoze:
            return "cannot bulldoze"
        else:
            return "bulldozing!!!!!!!"

if __name__ == "__main__":
    vehicle_1 = Vehicle("vehicle", "gas")
    print(vehicle_1.type, vehicle_1.fuel_type)
    print(vehicle_1.run())

    print("--------------------------------")

    car_1 = Car("car", "gas", 5000)
    print(car_1.run())
    print(car_1.type, car_1.fuel_type)
    print(car_1.display_gas())

    print("--------------------------------")

    bulldozer_1 = Bulldozer("bulldozer", "diesel", True)
    print(bulldozer_1.type, bulldozer_1.fuel_type)
    print(bulldozer_1.run())
    print(bulldozer_1.bulldoze())