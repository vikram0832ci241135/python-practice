"""Practice: variables and basic input."""


# Q1: Take the user's name, age, and city, then print them.
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")


# Q2: Convert Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")
