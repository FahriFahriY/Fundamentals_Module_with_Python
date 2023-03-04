first_sting, second_sting = input().split()
total_sum = 0

if len(first_sting) < len(second_sting):
    for i in range(len(first_sting), len(second_sting)):

        total_sum += ord(second_sting[i])
elif len(first_sting) > len(second_sting):

    for i in range(len(second_sting), len(first_sting)):
        total_sum += ord(first_sting[i])

for i in range(min(len(first_sting), len(second_sting))):
    total_sum += ord(first_sting[i]) * ord(second_sting[i])

print(total_sum)
