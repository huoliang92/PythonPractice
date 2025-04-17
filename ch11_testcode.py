def city_country(city, country, population=None):
    if population:
        combo = f"{city.title()},{country.title()} -population {population} "
    else:
        combo = f"{city.title()},{country.title()}"
    return combo


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, upSalary=50):
        self.salary += upSalary
        return self.salary