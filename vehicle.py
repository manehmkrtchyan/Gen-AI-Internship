class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def sound(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return super().display_info() + f", {self.num_doors} doors"

    def sound(self):
        return "Vroom Vroom!"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, num_wheels):
        super().__init__(brand, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        return super().display_info() + f", {self.num_wheels} wheels"

    def sound(self):
        return "Vroom!"


class Bicycle(Vehicle):
    def __init__(self, brand, model, year, num_gears):
        super().__init__(brand, model, year)
        self.num_gears = num_gears

    def display_info(self):
        return super().display_info() + f", {self.num_gears} gears"

    def sound(self):
        return "Ring ring!"


if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2022, 4)
    motorcycle = Motorcycle("Honda", "CBR500R", 2021, 2)
    bicycle = Bicycle("Trek", "FX 3", 2020, 18)

    vehicles = [car, motorcycle, bicycle]

    for vehicle in vehicles:
        print(vehicle.display_info())
        print(vehicle.sound())
        print()
