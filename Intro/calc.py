# description
"""
author: Andrew Singo
System: Simple Python Calculator
"""

# imports
from display import print_menu, print_header

# global vars

# functions



# direct instructions
print_header()
print_menu()

option = input("Select an option: ")

num1 = float(input("Please provide num1: "))
num2 = float(input("Please provide num2: "))
message = input("Please Type Message: ")

if option == "1":
    res = num1 + num2
    
elif option == "2":
    res = num1 - num2
   
elif option == "3":
    res = num1 * num2
    
elif option == "4":
    res = num1 / num2
    if num2 == 0:
        print("ERROR System cannot divide into 0")
        res = "ERROR!"




print(f"the Result is: {res}")    

