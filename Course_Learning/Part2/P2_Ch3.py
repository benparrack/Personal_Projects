num = 7

if num >= 6 and num <= 8: # can do and conditionals to test multiple conditions at once, both need to be true to result in true
    print("You're number is between 6-8!")

if num <= 6 or num >= 8: # can do or conditionals to test multiple conditions at once, only one needs to be true to result in true
    print("This is literally every single number except for 7")

if not (num <= 6 and num >= 8): # not can be used to get the opposite result
    print("I don't know at this point")

if 5 < num < 9: # this is a shorthand python allows for checking if a num is between two other numbers, or a range
    print("yay!")    

if True:  # nested conditionals; where the conditional inside the other only runs if the first one is true
    if False:
        print("I'll never run ):")


    

