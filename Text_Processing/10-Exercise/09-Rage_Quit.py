string = input()

unique_letters = []
result, currently_string = "", ""

for i in range(len(string)):
    if string[i].isdigit():

        if i + 1 < len(string) and string[i + 1].isdigit():
            number = int(string[i:i+2])
        else:
            number = int(string[i])

        currently_string *= number
        result += currently_string
        currently_string = ""

    else:
        char = string[i].upper()
        if char not in unique_letters:
            unique_letters.append(char)
        currently_string += char

print(f"Unique symbols used: {len(unique_letters)}")
print(result)
