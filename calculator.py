import math
import sympy as sp

# Define a restricted set of allowed functions and operators for the scientific calculator
allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

# Add more scientific functions to the allowed names
allowed_names.update({
    'abs': abs,              # Absolute value
    'pow': pow,              # Power (x ** y)
    'factorial': math.factorial,  # Factorial (from math)
    'log': math.log,         # Natural log (log base e)
    'log10': math.log10,     # Log base 10
    'exp': math.exp,         # Exponential function (e^x)
    'pi': math.pi,           # Pi constant
    'e': math.e,             # Euler's constant
    'sin': math.sin,         # Sine function (radians)
    'cos': math.cos,         # Cosine function (radians)
    'tan': math.tan,         # Tangent function (radians)
    'asin': math.asin,       # Inverse sine
    'acos': math.acos,       # Inverse cosine
    'atan': math.atan,       # Inverse tangent
    'sinh': math.sinh,       # Hyperbolic sine
    'cosh': math.cosh,       # Hyperbolic cosine
    'tanh': math.tanh,       # Hyperbolic tangent
    'degrees': math.degrees, # Convert radians to degrees
    'radians': math.radians, # Convert degrees to radians
    'sqrt': math.sqrt,       # Square root
})

# Remove dangerous built-ins for security
allowed_names.update({"__builtins__": {}})

# Function to calculate expression for the scientific calculator
def calculate_expression(expr):
    try:
        # Use eval with the restricted environment and allowed functions
        result = eval(expr, {"__builtins__": None}, allowed_names)
        return result
    except Exception as e:
        return f"Error: {e}"

# Function to calculate the factorial (for the factorial calculator)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Unified main function that gives the user both calculators
def main():
    print("Welcome to the Rojak Calculator!")
    print("You can use two different calculators here:")
    print("1. Press 'S' to use the **Scientific Calculator** with functions like sin(), cos(), log(), sqrt(), etc.")
    print("2. Press 'F' to use the **Factorial Calculator** to calculate the factorial of a number.")
    print("If you want to exit the program at any time, just type 'exit'.")

    while True:
        # Prompt user to choose between scientific or factorial calculator
        calculator_type = input("Please choose 'S' for Scientific Calculator or 'F' for Factorial Calculator (or 'exit' to quit): ").strip().lower()

        if calculator_type == 'exit':
            print("Thank you for using the Rojak Calculator! Goodbye!")
            break

        elif calculator_type == 's':
            # Scientific Calculator Mode
            while True:
                expression = input("You are now in the **Scientific Calculator** mode.\nEnter a mathematical expression to calculate (or type 'back' to return to the main menu, 'exit' to quit): ")

                if expression.lower() == 'back':
                    break  # Break out of the scientific calculator mode and return to the main menu

                elif expression.lower() == 'exit':
                    print("Thank you for using the Rojak Calculator! Goodbye!")
                    return  # Exit the entire program

                result = calculate_expression(expression)
                print(f"Result: {result}")

        elif calculator_type == 'f':
            # Factorial Calculator Mode
            while True:
                # Allow the user to input either an integer or "back" to return to the main menu, or "exit" to quit
                n_input = input("You are now in the **Factorial Calculator** mode.\nEnter a positive integer to calculate its factorial (or type 'back' to return to the main menu, 'exit' to quit): ")

                if n_input.lower() == 'back':
                    break  # Break out of the factorial calculator mode and return to the main menu

                elif n_input.lower() == 'exit':
                    print("Thank you for using the Rojak Calculator! Goodbye!")
                    return  # Exit the entire program

                try:
                    n = int(n_input)
                    if n < 0:
                        print("Please enter a **positive integer**.")
                        continue
                    else:
                        fact = factorial(n)
                        print(f"The factorial of {n} is {fact}")
                        break  # After calculating factorial, exit this mode and return to the main menu
                except ValueError:
                    print("Please enter a **valid integer**.")

        else:
            print("Invalid input. Please choose 'S' for Scientific Calculator or 'F' for Factorial Calculator.")

if __name__ == "__main__":
    main()
