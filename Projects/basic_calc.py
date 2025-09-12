# this will the be the simplest calculator format possible, eventually with a future project being a full functioning popup window
type = input("Would you like to add, subtract, multiple, or divide? Type +, -, *, or / : ")

while type != "+" and type != "-" and type != "*" and type != "/":
    type = input("It seems as though you have chosen an incorrect function. Please type +, -, *, or / : ")
print("Thanks!")

if type == "+":
    num1 = int(input("What is the first number in the equation? "))
    num2 = int(input("What is the second number in the equation? "))
    total = num1 + num2
    yesno = input("Would you like to compute another number? y/n: ")
    while yesno == "y":
        num3 = int(input("What is the second number in the equation? "))
        total = num3 + total
        yesno = input("Would you like to compute another number? y/n: ")
    print(f"Your total is {total}! Thanks for using this calculator")

if type == "-":
    num1 = int(input("What is the first number in the equation? "))
    num2 = int(input("What is the second number in the equation? "))
    total = num1 - num2
    yesno = input("Would you like to compute another number? y/n: ")
    while yesno == "y":
        num3 = int(input("What is the next number in the equation? "))
        total = total - num3
        yesno = input("Would you like to compute another number? y/n: ")
    print(f"Your total is {total}! Thanks for using this calculator")

if type == "*":
    num1 = int(input("What is the first number in the equation? "))
    num2 = int(input("What is the second number in the equation? "))
    total = num1 * num2
    yesno = input("Would you like to compute another number? y/n: ")
    while yesno == "y":
        num3 = int(input("What is the next number in the equation? "))
        total = num3 * total
        yesno = input("Would you like to compute another number? y/n: ")
    print(f"Your total is {total}! Thanks for using this calculator")

if type == "/":
    num1 = int(input("What is the first number in the equation? "))
    num2 = int(input("What is the second number in the equation? "))
    total = num1 / num2
    yesno = input("Would you like to compute another number? y/n: ")
    while yesno == "y":
        num3 = int(input("What is the next number in the equation? "))
        total = total / num3
        yesno = input("Would you like to compute another number? y/n: ")
    print(f"Your total is {total}! Thanks for using this calculator")

