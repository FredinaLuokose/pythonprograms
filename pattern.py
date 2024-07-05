def print_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

rows = int(input("Enter the number of rows for the triangle: "))
print_triangle(rows)



def print_number_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

rows = int(input("Enter the number of rows for the number triangle: "))
print_number_triangle(rows)
