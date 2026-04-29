# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers (with zero check)
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    # Loop continuously until user chooses to exit
    while True:
        # Display the menu options to the user
        print("Simple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        # Get user's choice
        choice = input("Choose an operation (1-5): ")
        
        # Check if user wants to exit
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        # Process calculations for options 1-4
        if choice in ('1', '2', '3', '4'):
            # Try to get two numbers from the user
            try: 
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            # Handle case where user enters non-numeric values
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            # Perform the selected operation and display result
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        # Handle invalid menu choices
        else:
            print("Invalid choice. Please select a valid option.")

# Run the calculator program when this script is executed
if __name__ == "__main__":
   calculator()