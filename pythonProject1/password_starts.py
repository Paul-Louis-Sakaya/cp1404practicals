

print("\t\t\tJCU\n*system Log in*")
username = input('Please enter your name:')
pin = input("Please enter your password:")

default_pin = "paulsakaya"
if len(pin)<=4:
    print("Thanx")
    print("Successfuly loged in")
elif len(pin)>4:
    if default_pin == pin:
        print("Successfuly loged in")
    else:
       print("Sorry....\nNot system default:")
else:
    print("Sorry")
    print("Please enter a valid password:")

print("\n\t~~~All rights reserved~~~")

