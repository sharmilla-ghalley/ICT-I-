# Start the main calculator loop
while True:
    # Display the calculator menu
    print("Simple Calculator")
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Exit")
    
    # Get the user's menu choice
    choice = input("Choose an option (1-5): ")

    # Check if user selected exit option
    if choice == '5':
        print("Goodbye!")
        break

    # Check if user selected a valid operation (1-4)
    if choice in ['1', '2', '3', '4']:
        try:
            # Get the first number from user
            num1 = float(input("Enter first number: "))
            # Get the second number from user
            num2 = float(input("Enter second number: "))

            # Addition operation
            if choice == '1':
                print(f"Result: {num1 + num2}")
            # Subtraction operation
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            # Multiplication operation
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            # Division operation with zero check
            elif choice == '4':
                # Check if second number is zero
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print(f"Result: {num1 / num2}")
                    
        # Handle case where user enters non-numeric values
        except ValueError:
            print("Error: Please enter valid numbers.")
    # Handle invalid menu choices
    else:
        print("Invalid choice, please try again.") 
