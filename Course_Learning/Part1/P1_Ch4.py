num1 = 2.5
num2 = 5.17
num3 = 9.43

mean = (num1 + num2 + num3) // 3 # use two slashes to do int division, gives truncated whole number, chops off dec
print(f"Average is {mean}")

mod = 5 % 3 # gives remained
print(f"Remainder of 5 / 3 is {mod}")

exp = 5 ** 3 # exponential - 5 ^ 3
print(f"5 to the power of 3 is {exp}")

# if even one number in a mathmatical sequence is a floating point number, the result will be a floating point
# with division, it always defaults to floating point even if all numbers are ints

x = 5
y = 4
print(f"You can also do math instead f-strings, ex: {x/y}")

inp = input("Give a number: ") # inputs default to strings, so if we want it to be an int we have to cast to int
num = int(inp)

flo = float(input("Give a number: ")) # can also skip a step, as well as cast to float

num = 5
num += 5 # can add and equate to variable in one line