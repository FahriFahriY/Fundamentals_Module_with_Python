string = input()

for char in string:
    new_char = chr(ord(char) + 3)
    print(new_char, end="")
