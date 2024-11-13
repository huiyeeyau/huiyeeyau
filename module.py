#Random
import random

coin = random.choice(["heads", "tails"])    # Simulate a coin flip using random.choice
print(coin)

number = random.randint(1, 10)              # Generate a random number between 1 and 10
print(number)

#Statistics
import statistics
print(statistics.mean([100, 80]))

#Sys
import sys

for name in sys.argv[1:]:
    print("Hello my name is", name)
