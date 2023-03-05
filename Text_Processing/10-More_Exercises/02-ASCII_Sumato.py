first_character = input()
second_character = input()
string = input()

ascii_dictionary = {chr(x): x for x in range(ord(first_character)+1, ord(second_character))}

total_sum = 0
for char in string:
    if char in ascii_dictionary:
        total_sum += ascii_dictionary[char]

print(total_sum)
