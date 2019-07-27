'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

input_fahrenheit = float(input("Enter temperature in Fahrenheit :"))
celsius = (input_fahrenheit - 32) * (5 / 9)
print(str(input_fahrenheit) + " degress fahrenheit = " + str(celsius + " degrees celsius")