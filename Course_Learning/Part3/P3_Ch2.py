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

print(input_string[-1]) # -1 index prints the last character, or last thing in the array

input_string = "presumptious"

print(input_string[0:3]) # this is a substring, prints the letters from index 0 to 3, with 0 being included and 3 not
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])

bool = ("ello" in "Hello") # true, in is a conditional that checks if string a is a substring of b

input_string = "test"

print(input_string.find("t")) # 0   find prints the index of the first character if it is in string, -1 if not
print(input_string.find("x")) # -1 
print(input_string.find("es")) # 1
print(input_string.find("ets")) # -1


