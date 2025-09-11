def hello_world():
    print("Hows it going world")

hello_world()

#to run script do: python <filename>, and include the file extension

one = 1
two = 2
three = one + two
print(three)

#most variables in python seem to be floats, meaning they figure it out themselves

#if running from terminal, have to manually save before running or wont run changes

def calculator():
    num1 = int(input("Number 1 "))
    num2 = int(input("Number 2 "))
    total = num1 + num2
    print("Your added total is", total) 
#this is most basic way of adding an int to a string, could also cast total as a str

def calculator2():
    num1 = int(input("Number 1 "))
    num2 = int(input("Number 2 "))
    total = str(num1 + num2)
    print("Your added total is " + total) 

number1 = 5
number2 = 7
def calculatorPre():
    total = str(number1 + number2)
    print("Your added total is " + total) 

#you can also variables not from the loop, but you cannot use values initialized in the loop outside the loop

#calculator()
#calculator2()
calculatorPre()

#since you dont specify variable type in python, have to cast type in parenthesis like: int(str)


name = "Alice"
print("Hi, " + name + "!")



print(2 + 2) # you can do math inside print statements

#print(""Hi!"") # this doesnt work
print('"Hi!"') # this does, have to use single quotes to print out quotes


