# commission_employee.py

class CommissionEmployee:
    def __init__(self, first_name, last_name, social_security_number, gross_sales, commission_rate):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_social_security_number(social_security_number)
        self.set_gross_sales(gross_sales)
        self.set_commission_rate(commission_rate)

    # Getter and Setter for first name
    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        if not first_name:
            raise ValueError("First name cannot be empty.")
        self._first_name = first_name

    # Getter and Setter for last name
    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        if not last_name:
            raise ValueError("Last name cannot be empty.")
        self._last_name = last_name

    # Getter and Setter for social security number
    def get_social_security_number(self):
        return self._social_security_number

    def set_social_security_number(self, social_security_number):
        if not social_security_number:
            raise ValueError("Social Security Number cannot be empty.")
        self._social_security_number = social_security_number

    # Getter and Setter for gross sales
    def get_gross_sales(self):
        return self._gross_sales

    def set_gross_sales(self, gross_sales):
        if gross_sales < 0:
            raise ValueError("Gross sales must be greater than or equal to 0.0.")
        self._gross_sales = gross_sales

    # Getter and Setter for commission rate
    def get_commission_rate(self):
        return self._commission_rate

    def set_commission_rate(self, commission_rate):
        if commission_rate < 0.0 or commission_rate > 1.0:
            raise ValueError("Commission rate must be between 0.0 and 1.0.")
        self._commission_rate = commission_rate

    # Method to calculate earnings
    def earnings(self):
        return self.get_gross_sales() * self.get_commission_rate()

    # Method to display the employee's details
    def __str__(self):
        return (f"CommissionEmployee: {self.get_first_name()} {self.get_last_name()}, "
                f"SSN: {self.get_social_security_number()}, Gross Sales: ${self.get_gross_sales():.2f}, "
                f"Commission Rate: {self.get_commission_rate():.2f}, Earnings: ${self.earnings():.2f}")
