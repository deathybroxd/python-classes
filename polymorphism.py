class Car:
    def __init__(self, model, can_drive):
        self.model = model
        self.can_drive = can_drive
    
    def drive(self):
        if self.can_drive:
            return f"{self.model} vrooms in a basic ass car"
        else:
            return "basic ahh car no go"
        
class Toyota_Corolla(Car):
    def __init__(self, model, can_drive):
        super().__init__(model, can_drive)
    
    def drive(self):
        if self.can_drive:
            return f"{self.model} vrooms by making electricity with footsteps"
        else:
            return "toyota corolla no go"
        
    def boom(self):
        return "corolla go boom"
        
class Toyota_Camry(Toyota_Corolla):
    def __init__(self, model, can_drive):
        super().__init__(model, can_drive)

    def drive(self):
        if self.can_drive:
            return f"{self.model} vrooms by making electricity with footsteps slightly faster"
        else:
            return "toyota camry no go"
        
if __name__ == "__main__":
    car_1 = Car("Car 1", True)
    car_2 = Car("Car 2", False)
    print(car_1.drive())
    print(car_2.drive())

    print("--------------------------------")

    toyota_corolla_1 = Toyota_Corolla("2006 Toyota Corolla", True)
    toyota_corolla_2 = Toyota_Corolla("2009 Toyota Corolla", False)
    print(toyota_corolla_1.drive())
    print(toyota_corolla_2.drive())
    print(toyota_corolla_1.boom())
    print(toyota_corolla_2.boom())

    print("--------------------------------")

    toyota_camry_1 = Toyota_Camry("2007 Toyota Camry", True)
    toyota_camry_2 = Toyota_Camry("2019 Toyota Camry", False)
    print(toyota_camry_1.drive())
    print(toyota_camry_2.drive())
    print(toyota_camry_1.boom())
    print(toyota_camry_2.boom())
