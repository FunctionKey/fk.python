### EP 1

# Print function
print("Hello world!")

# Print multiple lines
print("""Hello World!
This is me.""")

# Print a new line inside a string
print("Hello \n World")

# Concatonate strings
print("Hello " + "World!")

# Repeat strings
print("Hello" * 100)

### EP 2

print("Hello, welmoce to the coffee shop")
#print("What is your name?")

# Input function and save it to a variable
name = input("What is your name?\n")

# Print input results
#print(input("What is your name?"))
#print(name)

# Print string concatenated with variable
print("Hello " + name + ", thank you so much for coming in today!")

# Menu scenario
menu = "- coffee\n- milk\n- cappucino"
order = input("Hi " + name +", here's our menu.\n" + menu + "\n\nWhat would you like today?\n")

#order = input()
print("Ok " + name + ", a " + order + " coming right out! Thank you!")

### EP 3

# Strings
name = "Filipe"
age = 7
print(name)
print(age)

# Check what type of object is saved on a string
print(type(name))
print(type(age))

# Number with decimal values are floating point numbers (or just "floats")
actual_age = 7.95
print(type(actual_age))

# Calculator
# add
print(5 + 7)
# devide
print (5 / 7)
# multiply
print (5 * 7)
# 5 to the 7th power
print (5 ** 7)
# math functions
print(5 ** 7 + 6 / 9 * 6 - 4)
math = 5 ** 7 + 6 / 9 * 6 - 4
print (math)

results = age + actual_age + math
print(results)