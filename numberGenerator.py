import random

# Generate a list of 10 random numbers
random_numbers = []
for _ in range(10):
    random_numbers.append(random.randint(1, 100))

print(random_numbers)