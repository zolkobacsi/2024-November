number_list = [3, 7, 2, 9, 5]
highest = number_list[0]

for i in number_list:
    if i > highest:
        highest = i

print(highest)