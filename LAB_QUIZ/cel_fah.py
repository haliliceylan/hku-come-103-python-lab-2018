# Converts from Celsius to Farenheit
def celsiusToFahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit


# Converts from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
