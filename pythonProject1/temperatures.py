

fahrenheit = 31
celsius = 42

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
