# Base class: CommissionEmployee
class CommissionEmployee:
    def __init__(self, first_name, last_name, social_security_number, gross_sales, commission_rate):
        self._first_name = first_name
        self._last_name = last_name
        self._social_security_number = social_security_number
        self._gross_sales = max(0.0, gross_sales)  # Ensuring gross_sales is non-negative
        self._commission_rate = commission_rate if 0.0 <= commission_rate <= 1.0 else 0.0  # Validating commission_rate

    # Method to calculate earnings
    def earnings(self):
        return self._gross_sales * self._commission_rate

    # Display Employee Details
    def display_employee_details(self):
        print(f"Employee: {self._first_name} {self._last_name}")
        print(f"SSN: {self._social_security_number}")
        print(f"Gross Sales: {self._gross_sales}")
        print(f"Commission Rate: {self._commission_rate}")
        print(f"Earnings: {self.earnings()}\n")


# Derived class: BasePlusCommissionEmployee
class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, first_name, last_name, social_security_number, gross_sales, commission_rate, base_salary):
        super().__init__(first_name, last_name, social_security_number, gross_sales, commission_rate)
        self._base_salary = max(0.0, base_salary)  # Ensuring base_salary is non-negative

    # Override earnings method
    def earnings(self):
        return self._base_salary + (self._gross_sales * self._commission_rate)

    # Method to set base salary with validation
    def set_base_salary(self, new_salary):
        if new_salary >= 0.0:
            self._base_salary = new_salary

    # Override display_employee_details method
    def display_employee_details(self):
        super().display_employee_details()
        print(f"Base Salary: {self._base_salary}")
        print(f"Total Earnings: {self.earnings()}\n")


# Implementation Tasks

# A. Create an instance of a Commission-Only Employee
commission_employee = CommissionEmployee("John", "Doe", "123-45-6789", 5000.0, 0.1)

# B. Create an instance of a BasePlusCommission Employee
base_plus_employee = BasePlusCommissionEmployee("Alice", "Smith", "987-65-4321", 7000.0, 0.12, 3000.0)

# C. Display earnings for both employees
print("Commission-Only Employee Details:")
commission_employee.display_employee_details()

print("Base Plus Commission Employee Details:")
base_plus_employee.display_employee_details()

# D. Update base salary and display updated earnings
base_plus_employee.set_base_salary(3500.0)

print("Updated Base Plus Commission Employee Details:")
base_plus_employee.display_employee_details()
