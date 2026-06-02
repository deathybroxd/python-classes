class Car:
    # constructor
    def __init__(self, engine, model, miles):
        self.engine = engine
        self.model = model
        self.miles = miles
    
    def start(self):
        if not self.engine:
            return f"No engine in this {self.model}"
        else:
            return f"{self.model} go vroom"
    
    def odometer(self):
        return f"{self.miles} miles on the dash"

if __name__ == "__main__":
    car_1 = Car(True, "2005 Toyota Corolla", 190000)
    car_2 = Car(False, "1994 Dodge Durango", 250000)

    print(car_1.model)
    print(car_1.start())
    print(car_1.odometer())
    print("------------------------")
    print(car_2.model)
    print(car_2.start())
    print(car_2.odometer())
