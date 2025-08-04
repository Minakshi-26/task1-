
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    else:
        return a / b

while True:
    print("--------------")
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("--------------")

    choice = input("Enter your choice (1 to 5): ")

    if choice == '5':
        print("Thank you for using the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    
        if choice == '1':
            result = add(num1, num2)
            print("Result = " + str(result))
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result = " + str(result))
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result = " + str(result))
        elif choice == '4':
            result = divide(num1, num2)
            print("Result = " + str(result))
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")