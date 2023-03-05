n = int(input())

for _ in range(n):
    string = input()

    name = string[string.index("@")+1:string.index("|")]
    age = string[string.index("#")+1:string.index("*")]

    print(f"{name} is {age} years old.")
