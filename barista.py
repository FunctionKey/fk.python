name = input("Hi, what is yout name?\n")

menu = "- coffee\n- milk\n- cappucino"
price = 8
order = input("Welcome " + name + ". Here is our menu:\n" + menu + "\nWhat would you like to order?\n")
quantity = input("And how many would you like?\n")
total = price * int(quantity)
#print(quantity)
#print(type(quantity))

print(quantity + " " + order + " comming right up! " + "The total will be " + str(total) + ", please.")