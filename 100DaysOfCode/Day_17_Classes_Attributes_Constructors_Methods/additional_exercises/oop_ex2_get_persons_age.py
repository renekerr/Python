# Create a person class. Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.

from datetime import date


class Person:
    """A class representing a person with attributes like name, country, and date of birth."""

    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age (self):
        """Calculates the person's age based on their date of birth."""
        current_date = date.today()
        age = current_date.year - self.date_of_birth.year
        # Check for birthday this year
        if current_date < date(current_date.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


person_sample = Person(name="Rene", country="Cuba", date_of_birth=date(1974, 5, 14))

print('Personal Information')
print(f'Name: {person_sample.name}')
print(f'Country: {person_sample.country}')
print(f'Date of birth: {person_sample.date_of_birth}')
print(f'Age: {person_sample.calculate_age()}')





