#Question 1-Declare a string variable. Use a method to convert it to lowercase.
text = "HELLO WORLD"

print(text.lower())

#Question 2-Create a list of 3 numbers. Use a method to add a fourth number
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

#Question 3-Create an object called car with: brand property ,method called describe that returns:
#This car is a Toyota ,Access and execute the method.
class Car:
    def __init__(self):
        self.brand = "Toyota"

    def describe(self):
        return f"This car is a {self.brand}"

car = Car()

print(car.describe())

#Question 4 (API Simulation)-Create an object called weatherAPI with a method getTemperature() that returns 28.
# Call the method and print the result.
class WeatherAPI:
    def getTemperature(self):
        return 28

weatherAPI = WeatherAPI()

print(weatherAPI.getTemperature())

