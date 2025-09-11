name = "Ben"
print(name) # you can print variables

name = "Addie"
print(name)

num_int = 100
num_string = "100"

print(num_int + num_int)
print(num_string + num_string) 
print(int(num_string) + int(num_string)) #can cast into to strings/floats if in form of int
#print(num_string / 2) doesnt work because is string, would work in int form or casted to int

#print("Number = " + num_int) throws error because are two different variable types
print("number = " + str(num_int)) #works because casted to string makes them the same type
print("number =", num_int) #also works because with commas variable type doesn't matter

print(f"The result is {num_int}") # this is an f string, gives more control of print functions, use {variable name}

name = "Ben"
age = 19
city = "Blacksburg"
print(f"Hi my name is {name}, im {age} years old, and I live in {city}") #demonstrates the use of f-string
print("Hi my name is", name, "I'm", age, "years old, and I live in", city) # also works, but more tedious

num1 = 2.5 # these are floating point variables, ie numbers with decimnals (doubles in java)
num2 = 5.17
num3 = 9.43

mean = (num1 + num2 + num3) / 3
print(f"Average is {mean}")

num4 = 2
num5 = 5
num6 = 9
mean2 = (num4 + num5 + num6) / 3
print(f"Average is {mean2}") # seems like python does decimals even for ints when doing math, which is really nice

