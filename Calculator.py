def calculator():
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt the user to choose an operation
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    # Perform the chosen operation
    if operation == '1':
        result = num1 + num2
        operation_sign = '+'
    elif operation == '2':
        result = num1 - num2
        operation_sign = '-'
    elif operation == '3':
        result = num1 * num2
        operation_sign = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_sign = '/'
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation choice. Please choose a valid operation (1/2/3/4)."
    
    # Display the result
    return f"The result of {num1} {operation_sign} {num2} is: {result}"

# Call the calculator function
print(calculator())
