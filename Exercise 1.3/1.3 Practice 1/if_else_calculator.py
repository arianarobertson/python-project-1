val1 = float(input("Enter the first number: "))
val2 = float(input("Enter the second number: "))
operator = input("Enter '+' for addition or '-' for subtraction: ")

if operator == '+':
    result = val1 + val2
    print("Result:", result)
elif operator == '-':
    result = val1 - val2
    print("Result:", result)
else:
    print("Unknown operator")
