print("Welcome")

name = input("What's your name?\n")

if name == "ben" or name == "ann":
    evil = input("Are you evil?\n")
    if evil == "yes":
        deeds = int(input("How many good deeds did you do today?\n"))
        if deeds < 4:
            print("Your are not welcome.")
            exit()  # If this is true exit program
        else:
            print("Ok, you can come in this time.")
    else:
        print("Hello " + name + ", thanks for coming!\n")
else:
    print("Hello " + name + ", thanks for coming!\n")