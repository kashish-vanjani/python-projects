import random
import string

print("Welcome to the Password Generator!")

# get length with basic validation
try:
    length = int(input("Enter password length: "))
    if length < 1:
        raise ValueError
except ValueError:
    print("Invalid input; using default length = 12.")
    length = 12

# all possible characters
characters = string.ascii_letters + string.digits + string.punctuation

# generate
password = ''.join(random.choice(characters) for _ in range(length))

# output
print(f"Your generated password is: {password}")
