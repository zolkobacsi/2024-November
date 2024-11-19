def find_max(number_list):
    result = number_list[0]
    for i in number_list:
        if i > result:
            result = i
    return result

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, -7, 17]

print(find_max(number_list))

