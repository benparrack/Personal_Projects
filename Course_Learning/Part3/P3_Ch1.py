a = 1
while a < 5:
    print(a)
    a += 1

print("Done!")

number = int(input("Please type in a number: "))

while number < 100 and number % 5 != 0:
    print(number)
    number += 3

words = "pride"
words = words + ", prejudice"
words += " and python" # += also works for strings

print(words)


course = "Introduction to Programming"
grade = 4

verdict = "You have received "
verdict += f"the grade {grade} " # fstrings can also be used when building strings
verdict += f"from the course {course}"

print(verdict)

word = "banana"
print(word*3) # besides just adding strings together, you can also multiply which will give "bananabananabanana"

n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

length = len("Hi") # int = 2

#this is an interesting way of "underlining" a word
input_string = input("Please type in a string: ") 
print(input_string)
print("-"*len(input_string))

#all strings characters have indices from 0:len-1, and can be retrived quite easily
input_string = input("Please type in a string: ")
print(input_string[0])
print(input_string[1])
print(input_string[3])