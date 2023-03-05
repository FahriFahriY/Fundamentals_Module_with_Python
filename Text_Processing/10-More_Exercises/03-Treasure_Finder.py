numbers = [int(x) for x in input().split()]
string = input()


while string != "find":
    result = ""
    i = 0
    for char in string:
        result += chr(ord(char) - numbers[i])
        i = (i + 1) % len(numbers)

    start_idx = result.index("&") + 1
    prize = result[start_idx:result.index("&", start_idx)]
    coordinates = result[result.index("<") + 1:result.index(">")]

    print(f"Found {prize} at {coordinates}")

    string = input()
