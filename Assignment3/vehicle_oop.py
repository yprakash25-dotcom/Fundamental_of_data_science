"""Program to demonstrate inheritance with Vehicle and Car classes."""


class Vehicle:
    """Base vehicle class with basic details."""

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def display_info(self) -> None:
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    """Car class that extends Vehicle by adding fuel type."""

    def __init__(self, make: str, model: str, year: int, fuel_type: str) -> None:
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def display_info(self) -> None:
        print(f"{self.year} {self.make} {self.model} ({self.fuel_type})")


if __name__ == "__main__":
    print("Vehicle OOP Program")
    cars: list[Car] = []

    for i in range(1, 4):
        print(f"\nEnter details for car {i}:")
        make = input("Make: ").strip()
        model = input("Model: ").strip()
        try:
            year = int(input("Year: ").strip())
        except ValueError:
            year = 0
            print("Invalid year entered; using 0.")
        fuel_type = input("Fuel type: ").strip()
        cars.append(Car(make, model, year, fuel_type))

    print("\nCars entered:")
    for car in cars:
        car.display_info()
