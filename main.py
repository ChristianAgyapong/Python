# main.py
from commission_employee import CommissionEmployee

def main():
    try:
        # Create a CommissionEmployee object
        employee = CommissionEmployee("John", "Doe", "123-45-6789", 50000.0, 0.1)

        # Display employee details
        print(employee)

        # Update gross sales and commission rate
        employee.set_gross_sales(60000.0)
        employee.set_commission_rate(0.12)

        # Display updated employee details
        print("\nUpdated Employee Details:")
        print(employee)

        # Calculate and display earnings
        print(f"\nEmployee's Earnings: ${employee.earnings():.2f}")

        # Test invalid values (this should raise exceptions)
        try:
            employee.set_gross_sales(-1000.0)  # Invalid gross sales
        except ValueError as e:
            print(f"\nError: {e}")

        try:
            employee.set_commission_rate(1.5)  # Invalid commission rate
        except ValueError as e:
            print(f"\nError: {e}")

    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()

