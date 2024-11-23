from sympy import symbols, diff, sin, cos, tan, sec, cot, csc

def calculate_derivative():
    while True:
        try:
            # Instructions for the user on how to input the expression
            print("\nInstructions for Input:")
            print("1. Use '**' for powers. For example, to write 3x square, use '3*x**2'.")
            print("2. For trigonometric functions, use")
            print("    'sin(x)', 'cot(x)' etc")
            print("\n---")
            
            # Taking input
            expression = input("Enter the mathematical expression: ")
            variable = input("\nEnter the variable to differentiate with respect to (e.g., x): ")

           
            expression = expression.replace("^", "**")

           
            var = symbols(variable)
            
          
            func = eval(expression, {"sin": sin, "cos": cos, "tan": tan, "sec": sec, "cot": cot, "csc": csc, "x": var, "y": var, "z": var})
            
            # Calculating the derivative
            derivative = diff(func, var)
            
            # Display the result
            print(f"\nThe derivative of {expression} with respect to {variable} is: {derivative}")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Please ensure your input is a valid mathematical expression and variable.")
            print("Try again.\n")

# Run the program
if __name__ == "__main__":
    calculate_derivative()
