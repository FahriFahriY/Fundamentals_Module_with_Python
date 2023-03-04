string = input()

currently_char = ""

for char in string:
    if currently_char != char:
        print(char, end="")
        currently_char = char
