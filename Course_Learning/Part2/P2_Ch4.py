while True: # runs while the conditional statement is true
    print("This is going to print forever!") # I ran this for some reason and it did run forever! Note to stop a program
    # hit ctrl + c. Sometimes need to hit c twice in quick succession to stop it
    break
# another way to kill a program without having the conditional be false, is to have a break

# a good way to use it is to have an if statement with the break inside it, so the loop can be terminated from a varaible outside
# of the original conditional statement

#for example:
while True:
    print("Hello")

    if int(input("Type 1 to die ")) == 1:
        break

# copied and pasted, felt to lazy to write my own version. Helper variable example:
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

    # this is printed if the code was incorrect AND there have been less than three attempts
    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")
    