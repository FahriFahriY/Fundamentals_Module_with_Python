string = input().split(":")


for i in range(1, len(string)):
    if string[i] == "":
        print("::")
    else:
        print(f":" + string[i][0])
