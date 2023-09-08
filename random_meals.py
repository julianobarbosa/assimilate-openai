import random

fruits = ["apple", "banana", "orange", "pear", "pineapple", "strawberry", "watermelon"]
dishes = ["pizza", "pasta", "burger", "steak", "salad", "soup", "chicken"]

meals = [f"{random.choice(fruits)} {random.choice(dishes)}" for _ in range(5)]
print(meals)
