strings = input().split()

for i in range(len(strings)):
    strings[i] = strings[i] * len(strings[i])

print("".join(strings))
