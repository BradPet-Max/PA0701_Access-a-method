#Question 1-Create an object product with:name ,price,stock ,Print each property separately.
class Product:
    def __init__(self):
        self.name = "Laptop"
        self.price = 15000
        self.stock = 20

product = Product()

print(product.name)
print(product.price)
print(product.stock)

#Question 2
class Weather:
    def __init__(self):
        self.city = "Polokwane"
        self.temperature = 28
        self.condition = "Sunny"

weather = Weather()

print(f"The temperature in {weather.city} is {weather.temperature} degrees")

#Question 3 – Nested Object
class Address:
    def __init__(self):
        self.city = "Pretoria"
        self.postalCode = 1  # 0001 becomes 1 in Python

class Company:
    def __init__(self):
        self.name = "Tech Solutions"
        self.address = Address()

company = Company()

print(company.address.postalCode)

#Question 4 – Method + Property
class Student:
    def __init__(self):
        self.name = "Peter"

class School:
    def getStudent(self):
        return Student()

school = School()

print(school.getStudent().name)