def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def main():
    print("Simple Calculator")
    
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "5":
            print("Goodbye!")
            break
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue
        
        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please choose from 1-5.")

if __name__ == "__main__":
    main()
