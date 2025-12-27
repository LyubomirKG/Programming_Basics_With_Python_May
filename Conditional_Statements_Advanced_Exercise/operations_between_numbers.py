# Input: two numbers and an arithmetic operation
num1 = int(input())
num2 = int(input())
operator = input()

result = ""

# Handling basic arithmetic operations with even/odd check
if operator in ['+', '-', '*']:
    if operator == '+':
        calc = num1 + num2
    elif operator == '-':
        calc = num1 - num2
    else:
        calc = num1 * num2
    
    even_odd = "even" if calc % 2 == 0 else "odd"
    result = f"{num1} {operator} {num2} = {calc} - {even_odd}"

# Handling division and modulo with zero check
elif num2 == 0:
    result = f"Cannot divide {num1} by zero"

elif operator == '/':
    calc = num1 / num2
    result = f"{num1} / {num2} = {calc:.2f}"

elif operator == '%':
    calc = num1 % num2
    result = f"{num1} % {num2} = {calc}"

print(result)
