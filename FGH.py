class CommissionEmployee:
    def __init__(self, first_name, last_name, social_security_number, gross_sales, commission_rate):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__social_security_number = social_security_number
        self.__gross_sales = max(0.0, gross_sales)  # Ensuring gross_sales is non-negative
        self.__commission_rate = commission_rate if 0.0 <= commission_rate <= 1.0 else 0.0  # Validating commission_rate

    # Getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_social_security_number(self):
        return self.__social_security_number

    def get_gross_sales(self):
        return self.__gross_sales

    def get_commission_rate(self):
        return self.__commission_rate

    # Setters
    def set_gross_sales(self, gross_sales):
        if gross_sales >= 0.0:
            self.__gross_sales = gross_sales

    def set_commission_rate(self, commission_rate):
        if 0.0 <= commission_rate <= 1.0:
            self.__commission_rate = commission_rate

    # Method to calculate earnings
    def earnings(self):
        return self.__gross_sales * self.__commission_rate

    # Display Employee Details
    def display_employee(self):
        print(f"Employee: {self.__first_name} {self.__last_name}")
        print(f"SSN: {self.__social_security_number}")
        print(f"Gross Sales: {self.__gross_sales}")
        print(f"Commission Rate: {self.__commission_rate}")
        print(f"Earnings: {self.earnings()}")


# Implementation Tasks

# Creating an instance of CommissionEmployee
employee = CommissionEmployee("John", "Doe", "123-45-6789", 5000.0, 0.1)

# Display Initial Employee Details
print("Initial Employee Details:")
employee.display_employee()

# Updating gross sales and commission rate
employee.set_gross_sales(7000.0)
employee.set_commission_rate(0.12)

# Display Updated Employee Details
print("\nUpdated Employee Details:")
employee.display_employee()
