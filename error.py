"""
1. SyntaxError
print("Hello, World!)

2. ValueError
num = int("hello")

3. TypeError
result = "hello" + 5

4. IndexError
my_list = [1, 2, 3]
print(my_list[5])

5. KeyError
my_dict = {"name": "Alice"}
print(my_dict["age"])

6. AttributeError
my_str = "hello"
my_str.append("world")

7. ImportError
import non_existent_module

8. NameError
print(undefined_variable)

9. ZeroDivisionError
result = 10 / 0

10. FileNotFoundError
with open("non_existent_file.txt", "r") as file:
    content = file.read()
"""

def main():
    result = divide()
    if result:
        print(result)

def divide():
    while True:
        try:
            num1_input = input("Enter the first number (or 'E' to exit): ")
            if num1_input.upper() == 'E':
                print("Exiting the program.")
                return None     # Exit the loop and function
            num1 = float(num1_input)

            num2_input = input("Enter the second number (or 'E' to exit): ")
            if num2_input.upper() == 'E':
                print("Exiting the program.")
                return None     # Exit the loop and function
            num2 = float(num2_input)

            result = num1 / num2
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")          # Handle division by zero
        except ValueError:
            print("Error: Both inputs must be numbers.")    # Handle wrong data types
        else:
            return f"The result of {num1} divided by {num2} is {result}"
            break

main()
