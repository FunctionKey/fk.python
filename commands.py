# REPL
# n1 = int(input("number 1: ")) ;\    # ;\ indicates REPL that there are multiple lines
# n2 = int(input("number 2: ")) ;\
# print("The sum is: ", n1 + n2)

print("hello world")
print(2*2)
print(2**2)
print(5/2)
print(5//2)
print(5%2)

print("what's up?")
# print('what's up?)  # returns error

# Variable
variable = "name"
print(variable)
print(type(variable))
variable = 10
print(variable)
print(type(variable))
#del variable
#print(variable)    # returns error

# Input
variable = input("create value \n")
print(variable)
print(type(variable))

# Conditional
# ==    Equal to
# !=    Not equal to
#  <    Less than
#  >    Greater than
# >=    Greater than or equal to
# <=    Less than or equal to
print(5==4)
print(5!=4)

kid = 8
age_to_school = 6

# Logic
if kid < age_to_school:
    print("kid should go be in pre-school \n")
elif kid == age_to_school:
    print("kid is accepted in school \n")
else:
    print("kid should be in another class \n")

# Functions
print("hello world without function")
print("hello world without function")
print("hello world without function")

def function_hello_world():  # def stands for "define"
    text = "hello world"
    print(text)
    print(text)
    print(text)
function_hello_world()

def function_hello_world(text):
    print(text)
    print(text)
    print(text)
function_hello_world("hello world with function")

def function_hello_world(x,text):
    for i in range(x):
        print(text)
function_hello_world(3,"for loop inside a function")

# Functions with if statment
def school_age_calculator(age,name):
    if age < 5:
        print("Enjoy the time! ", name, " is only ", age)
    elif age == 5:
        print("Enjoy kindergarten, ", name)
    else:
        print("They grow up so fast!")
school_age_calculator(99,"Jim")

# Get value from function
def add_ten_to_age(age):
    new_age = age + 10
    return new_age
future_age = add_ten_to_age(15)
print(future_age)

# Loops
#while
x = 0
while (x < 5):
    print(x)
    x = x + 1

#for
for x in range(5,10):
    print(x)

# Arrays
days = ["mon","tue","wed","thu","fri","sat","sun"]
for d in days:
    print(d)

for d in days:
    if (d=="thu"):break # stop if item if found
    print(d)

for d in days:
    if (d=="thu"):continue  # skip item if found
    print(d)

# Modules
# Check imported modules
dir()
# Import new modules
import math
from re import L
print("pi is ", math.pi)

# List
my_list = ["item 1", "item 2","item 3"]
print("my list 1: \n", my_list)

my_list_2 = ["item 4", "item 5"]
my_list = my_list + my_list_2   # order in which you add lists metters
print("my list 2: \n", my_list)

my_list.append("item 6")    # using "append" method you can only add one item
print("my list 3: \n", my_list)

my_list.extend(["item 7", "item 9"])    # using "extend" method you still can only add one item although that item can be a list with several items
print("my list 4: \n", my_list)

my_list.insert(0, "item 0") # insert new item on the indicated possition (this case: beggining)
print("my list 5: \n", my_list)

my_list.insert(-1,"item 8") # insert new item on the indicated possition (this case: second to last)
print("my list 6: \n", my_list)

#my_list.clear() # clears entire list

my_list.remove("item 3")    # you can only remove one item at a time
print("my list 7: \n", my_list)

my_list.pop(-2) # remove several items using index; pop also returns the deleted item
print("my list 8: \n", my_list)
