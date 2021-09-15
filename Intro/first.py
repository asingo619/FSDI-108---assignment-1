# this is a comment

print("Hello World!!")


# variables

name = "Andrew"
age = 100
total = 123.45
found = False
name = []

# math equations
print(age * 2)
print(total / 10)

# if statements - must follow indentation rule.
if (age  < 100):
    print("Age is just a NUMBER!!!")
    print("next line")
elif (age == 100):
    print("Almost there")
else:
    print("old man :(")    

# function
def hello():
    print("Hello there")
    print("I'm a function")


def play(num):
    print("your number")
    print(num)

    if(num < 5):
        print("Number to low")

# execute a function
hello()
hello()

play(5)

# arrays are *list* in python.