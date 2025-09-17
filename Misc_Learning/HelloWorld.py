# there is probably a muchhhhhhh easier way to do this, but I'm making this at the start of my learning journey to see how much
# better I can make it later on
letters = ""
num = 7
counter = 0
import time
while len(letters) < 13:
    print(letters + "a")
    time.sleep(0.03)
    if num == 0:
        letters = letters + "a"
        continue # kind of like a break statement, goes back to the of the while loop and ignores other conditionals below
    print(letters + "b")
    time.sleep(0.03)
    if num == 1:
        letters = letters + "b"
        continue
    print(letters + "c")
    time.sleep(0.03)
    if num == 2:
        letters = letters + "c"
        continue
    print(letters + "d")
    time.sleep(0.03)
    if num == 3:
        letters = letters + "d"
        num = 28
        continue
    print(letters + "e")
    time.sleep(0.0)
    if num == 4:
        letters = letters + "e"
        counter += 1
        num = 11
        continue
    print(letters + "f")
    time.sleep(0.03)
    if num == 5:
        letters = letters + "f"
        continue
    print(letters + "g")
    time.sleep(0.03)
    if num == 6:
        letters = letters + "g"
        continue
    print(letters + "h")
    time.sleep(0.03)
    if num == 7:
        letters = letters + "h"
        counter += 1
        num = 4
        continue
    print(letters + "i")
    time.sleep(0.03)
    if num == 8:
        letters = letters + "i"
        continue
    print(letters + "j")
    time.sleep(0.03)
    if num == 9:
        letters = letters + "j"
        continue
    print(letters + "k")
    time.sleep(0.03)
    if num == 10:
        letters = letters + "k"
        continue
    print(letters + "l")
    time.sleep(0.03)
    if num == 11:
        letters = letters + "l"
        counter += 1
        if counter == 4:
            num = 14
        if counter == 9:
            num = 3
        continue
    print(letters + "m")
    time.sleep(0.03)
    if num == 12:
        letters = letters + "m"
        continue
    print(letters + "n")
    time.sleep(0.03)
    if num == 13:
        letters = letters + "n"
        continue
    print(letters + "o")
    time.sleep(0.03)
    if num == 14:
        letters = letters + "o"
        num = 26
        counter += 1
        if counter == 8:
            num = 17
        continue
    print(letters + "p")
    time.sleep(0.03)
    if num == 15:
        letters = letters + "p"
        continue
    print(letters + "q")
    time.sleep(0.03)
    if num == 16:
        letters = letters + "q"
        continue
    print(letters + "r")
    time.sleep(0.03)
    if num == 17:
        letters = letters + "r"
        num = 11
        continue
    print(letters + "s")
    time.sleep(0.03)
    if num == 18:
        letters = letters + "s"
        continue
    print(letters + "t")
    time.sleep(0.03)
    if num == 19:
        letters = letters + "t"
        continue
    print(letters + "u")
    time.sleep(0.03)
    if num == 20:
        letters = letters + "u"
        continue
    print(letters + "v")
    time.sleep(0.03)
    if num == 21:
        letters = letters + "v"
        continue
    print(letters + "w")
    time.sleep(0.03)
    if num == 22:
        letters = letters + "w"
        num = 14
        continue
    print(letters + "x")
    time.sleep(0.03)
    if num == 23:
        letters = letters + "x"
        continue
    print(letters + "y")
    time.sleep(0.03)
    if num == 24:
        letters = letters + "y"
        continue
    print(letters + "z")
    time.sleep(0.03)
    if num == 25:
        letters = letters + "z"
        continue
    print(letters + ",")
    time.sleep(0.03)
    if num == 26:
        letters = letters + ","
        counter += 1
        num = 27
        continue
    print(letters + " ")
    time.sleep(0.03)
    if num == 27:
        letters = letters + " "
        counter += 1
        num = 22
        continue
    print(letters + "!")
    time.sleep(0.03)
    if num == 28:
        letters = letters + "!"
        counter += 1
        break