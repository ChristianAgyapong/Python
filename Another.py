from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    def __init__(self, vehicle_id: str, model: str, fuel_level: float):
        self.vehicle_id = vehicle_id
        self.model = model
        self.fuel_level = fuel_level

    def refuel(self, liters: float):
        self.fuel_level += liters
        print(f"Vehicle {self.model} refueled. Current fuel level: {self.fuel_level} liters")

    @abstractmethod
    def calculate_range(self):
        pass

# Derived Class
class Car(Vehicle):
    def __init__(self, vehicle_id: str, model: str, fuel_level: float, fuel_efficiency: float):
        super().__init__(vehicle_id, model, fuel_level)
        self.fuel_efficiency = fuel_efficiency
    
    # Overriding calculate_range
    def calculate_range(self):
        range_km = self.fuel_level * self.fuel_efficiency
        print(f"Car {self.model} can travel {range_km} km with current fuel level.")

# Independent Class
class TransportationManager:
    # Demonstrating runtime polymorphism
    def operate_vehicle(self, vehicle: Vehicle):
        vehicle.calculate_range()

# Implementation
if __name__ == "__main__":
    # A. Create Vehicles
    sedan = Car("C001", "Sedan", 50, 15)
    
    # B. Refuel Sedan
    sedan.refuel(20)
    
    # C. Use operate_vehicle()
    manager = TransportationManager()
    manager.operate_vehicle(sedan)
