from calcy import add, subtract, multiply, divide, Power

print("=== Welcome to Calculator ===")


try:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

except ValueError:
  print("please enter valid numbers")
except ZeroDivisionError:
   print("cannot divide by zero")   

while True:

    print("\nChoose Operation")
    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice =="6":
        print("Goodbye")
        break

    if choice =="1":
        result = add(num1, num2)

    elif choice =="2":
        result = subtract(num1, num2)

    elif choice =="3":
        result = multiply(num1, num2)

    elif choice =="4":
        if num2 != 0:
            result = divide(num1, num2)
        else:
            print("Cannot divide by zero")
            continue
    
    elif choice =="5":
        result = Power(num1, num2)

    else:
        print("Invalid choice")
        continue

    print("Result:", result)