def factorial(sample_number):
    if sample_number == 0 or sample_number == 1:
        return 1

    result = sample_number
    for i in range(sample_number-1, 1, -1):
        result *= i
    
    return result

sample_number = 6

print(factorial(sample_number))