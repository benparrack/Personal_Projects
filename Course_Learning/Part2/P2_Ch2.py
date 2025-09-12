num = int(input("Number plz: ")) # fast way to make input int

if num < 0:
    print("That's a terrible answer")
else: # runs if original if statement is false
    print("Ooh big number. Nice.")


if num < 20:
    print("Thats an okay number")
elif num > 50: # elif means "else if" so if first if isnt true but want to check something else, can have infinit elifs
    print("Thats a big number!")
else:
    print("Thats a pretty big number. Good job.")

