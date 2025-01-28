class Humans:
    def __init__(self, name, age, place, parents):  # Constructor
        self.name = name
        self.age = age
        self.place = place
        self.parents = parents

    def introduce(self):  # Method to introduce the human
        print(f"My name is {self.name}. I am {self.age} years old, I live in {self.place}, and my parents are {self.parents}.")

    def update_age(self):  # Method to update age
        new_age = input("Please enter your current age: ")
        try:
            self.age = int(new_age)
            print(f"Thank you! Your age has been updated to {self.age}.")
        except ValueError:
            print("Invalid input. Age must be a number.")

    def update_place(self):  # Method to update place of residence
        new_place = input("Where do you currently live? ")
        self.place = new_place
        print(f"Your place of residence has been updated to {self.place}.")

    def greet_user(self):  # Method to greet the user by their name
        print(f"Hello, {self.name}! Welcome!")

    def parent_details(self):  # Method to display parent details
        print(f"Your parents are {self.parents}.")

    def farewell(self):  # Method to bid farewell
        print(f"Goodbye, {self.name}! Have a great day!")


# Function to get user input and create a Humans object
def create_user():
    print("Welcome to the user registration system!")
    name = input("Enter your name: ")
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input. Age must be a number.")

    place = input("Enter the place where you live: ")
    parents = input("Enter the names of your parents (separated by a comma): ")

    user = Humans(name, age, place, parents)
    return user


# Main Program
def main():
    user = create_user()  # Create a user object
    print("\nThank you for providing your details!\n")
    user.introduce()  # Call introduce method

    while True:
        print("\nWhat would you like to do?")
        print("1. Update your age")
        print("2. Update your place of residence")
        print("3. See your parent details")
        print("4. Introduce yourself again")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            user.update_age()
        elif choice == "2":
            user.update_place()
        elif choice == "3":
            user.parent_details()
        elif choice == "4":
            user.introduce()
        elif choice == "5":
            user.farewell()
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Run the program
if __name__ == "__main__":
    main()
