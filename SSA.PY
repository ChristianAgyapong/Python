class Students:
    def __init__(self, Name, School, Age, Grade):  # Fixed __init__ method
        self.Name = Name
        self.School = School
        self.Age = Age
        self.Grade = Grade

    def AccessPupil(self):  # Fixed indentation
        print('My name is ' + self.Name + ', I am ' + str(self.Age) + ' years old and I am in '
              + str(self.Grade) + ' grade at ' + self.School)

# Create an object and call the method
Pa = Students('John', 'Kings', 12, 7)  # Fixed object instantiation
Pa.AccessPupil()
