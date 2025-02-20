from abc import ABC, abstractmethod

# Abstract Class
class Employee(ABC):
    def __init__(self, name: str, employee_id: str):
        self._name = name
        self._employee_id = employee_id
    
    # Getter methods
    def get_name(self):
        return self._name
    
    def get_employee_id(self):
        return self._employee_id
    
    # Abstract method
    @abstractmethod
    def calculate_pay(self):
        pass

# Derived Class
class FullTimeEmployee(Employee):
    def __init__(self, name: str, employee_id: str, salary: float):
        super().__init__(name, employee_id)
        self._salary = salary
    
    # Getter method for salary
    def get_salary(self):
        return self._salary
    
    # Implement abstract method
    def calculate_pay(self):
        return f"FullTimeEmployee Pay: {self._salary}"

# Instantiate a FullTimeEmployee object
employee = FullTimeEmployee("John Doe", "FT123", 5000.00)

# Display employee details
print("Employee Name:", employee.get_name())
print("Employee ID:", employee.get_employee_id())
print("Salary:", employee.get_salary())
print("Pay Calculation:", employee.calculate_pay())
