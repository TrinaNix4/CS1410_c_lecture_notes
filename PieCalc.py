'''
Author: Trina Nixon
Brief: Pie Calculator to calculate quarts and pints for a pie

'''
import math
PI = 3.14
QUART_INCHES = 69.3549
PINT_INCHES = 34.7664

diameter = float(input("Enter the pie pan diameter: "))
height = float(input("Enter the height of pie pan: "))

# V= PI r^2h
volume = PI * pow(diameter/2, 2) * height
quarts = volume / QUART_INCHES
pints = volume / PINT_INCHES

print("Quarts:", round(quarts, 1))
print("Pints:", round(pints, 1))
