def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not possible."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    while True:
        choice = input("Enter choice (1, 2, 3, 4): ")
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input.")
                continue
            if choice == '1':
                print(f"Addition of {num1} and {num2} is {add(num1, num2)}")
            elif choice == '2':
                print(f"Subtraction of {num1} and {num2} is {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Multiplication of {num1} and {num2} is {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Division of {num1} and {num2} is {divide(num1, num2)}")
            next_calculation = input("Do you want to perform another calculation? (y/n): ")
            if next_calculation.lower() != 'y':
                break
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
