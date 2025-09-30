def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
   if y == 0:
       print("Error ! Cannot divide through Zero, its illegal") 
   else:
    return x / y
        
    
while True:
    print("Simple Calculator")
    print("Select operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. EXIT")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting Calculator... Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        try:
            print(f"{num1} / {num2} = {num1 / num2}")
        except ZeroDivisionError:
            print("Error! cannot divide by zero, Its invalid")
    else:
        print("Invalid choice! Please select a valid option.")

