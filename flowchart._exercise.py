def generate_multiplication_table():
    # Prompt the user to enter the number for the multiplication table
    number = int(input("Enter the number for which you want the multiplication table: "))
    
    # Prompt the user to enter the limit up to which the table should be generated
    limit = int(input("Enter the limit up to which you want the table generated: "))
    
    # Generate and display the multiplication table
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

# Run the function
generate_multiplication_table()


def generate_right_triangle():
    # Prompt the user to enter the height of the triangle
    height = int(input("Enter the height of the triangle: "))
    
    # Generate and display the right triangle pattern
    for i in range(1, height + 1):
        print('*' * i)

# Run the function
generate_right_triangle()


def nested_loops_with_conditions():
    for i in range(1, 10):
        if i == 7:
            break
        for j in range(1, 10):
            if j == 3:
                continue
            print(j, end=' ')
        print()  # for a new line after inner loop

# Run the function
nested_loops_with_conditions()
