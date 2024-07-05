def cummilative_multiplication(numbers):
    cumilative_list = []
    total = 1
    for num in numbers:
        total *= num
        cumilative_list.append(total)
    return cumilative_list
    
numbers = [1,2,3,4]
result= cummilative_multiplication(numbers)
print(result)