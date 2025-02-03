
class Vehicle:

    total_vehicles = 0


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Vehicle.update_total_vehicles()


    @classmethod
    def update_total_vehicles(cls):
        cls.total_vehicles += 1


    def display_vehicle(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


car1 = Vehicle("Toyota", "Camry", 2020)
car2 = Vehicle("Ford", "Explorer", 2019)


car1.display_vehicle()
car2.display_vehicle()


print(f"Total Vehicles: {Vehicle.total_vehicles}")
