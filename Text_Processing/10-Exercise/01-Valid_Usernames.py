usernames = input().split(", ")
valid_username = []

for username in usernames:
    if 3 < len(username) < 16:
        for char in username:
            if not char.isalnum() and char not in ["-", "_"]:
                break
        else:
            valid_username.append(username)

print("\n".join(valid_username))
