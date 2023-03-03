string = input()

numbers, letters, other = "", "", ""

for char in string:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        other += char

print(numbers)
print(letters)
print(other)
