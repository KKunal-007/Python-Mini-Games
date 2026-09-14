# This script acts as a simple calculator that evaluates a mathematical expression entered by the user.

expression = input("Enter the expression : ") # Prompt the user to enter a math expression as a string (e.g., "2 + 3 * 4")
result = int(eval(expression)) # Evaluate the expression using eval(), then convert the result to an integer
print(f"{expression} = {result}") # Display the original expression and its


