path_to_file = input().split("\\")
name, extension = path_to_file[-1].split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")
