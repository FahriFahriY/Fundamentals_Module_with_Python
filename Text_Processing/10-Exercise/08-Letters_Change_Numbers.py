def position_in_alphabet(letter):
    return ord(letter.upper()) - 64


strings = input().split()
total_sum = 0

for string in strings:
    fist_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:len(string)-1])

    if fist_letter.isupper():
        number /= position_in_alphabet(fist_letter)
    else:
        number *= position_in_alphabet(fist_letter)

    if last_letter.isupper():
        number -= position_in_alphabet(last_letter)
    else:
        number += position_in_alphabet(last_letter)

    total_sum += number

print(f"{total_sum:.2f}")
