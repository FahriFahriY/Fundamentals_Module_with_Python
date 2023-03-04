string = input()
explosion_power = 0

result = ""
for i in range(len(string)):
    if explosion_power > 0 and string[i] != ">":
        explosion_power -= 1
    else:
        if string[i] == ">":
            explosion_power += int(string[i + 1])
        result += string[i]

print(result)
