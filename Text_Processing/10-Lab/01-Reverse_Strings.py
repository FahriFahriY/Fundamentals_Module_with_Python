word = input()

results = []
while word != "end":
    result = f"{word} = {word[::-1]}"
    results.append(result)

    word = input()

print("\n".join(results))
