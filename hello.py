print("Hello, World!")

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for i in range(1, n + 1):   # Start from 1 to n inclusive
    for j in range(i):      # Inner loop to print i asterisks
        print("*", end="")
    print()                 # Move to the next line after each row
