### Fixed Python
import random

a = random.randint(1, 12)
b = random.randint(1, 12)
for _ in range(1):
    question = f"What is {a} x {b}? "
    answer = input(question)
    if answer == str(a * b):
        print("Well done!")
    else:
        print("No.")
