print("Enter the first number:")
first_number = input()
print("Enter the second number:")
second_number = input()
print("Choose an operation(+, -, *, /):")
operation = input()
first_number = float(first_number)
second_number = float(second_number)
operation = operation.strip()
if operation == '+':
 result = first_number + second_number
elif operation == '-':
 result = first_number - second_number
elif operation == '*':
 result = first_number * second_number
elif operation == '/':
 result = first_number / second_number
else:
 print("You didn't choose a valid operation, choose among +, -, * and /.")
 operation = input()
print(f"The result is {result:.2f}")