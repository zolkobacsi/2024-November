def reverse_string(string):
    result = ""
    for i in reversed(string):
        result += i

    return result

string = "morning"

print(reverse_string(string))