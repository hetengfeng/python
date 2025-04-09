#!/usr/bin/env python3

import random 

MIN = 1
MAX = 1000

print("Welcome to Number Guessing Game!")
print(f"Please enter an integer between {MIN} and {MAX}")
print("-" * 30)

times = 0

random_number = random.randint(MIN, MAX)

while True:
    user_input = input(f"Attempt {times +1}: ")
    try:
        guess = int(user_input)
        if guess > MAX or guess < MIN:
            print("Your guess goes beyond the range, please try again.")
            continue
        times += 1
        if guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
        else:
            break
    except ValueError:
        print("Please enter an INTEGER!")

print(f"Congratulations! You succeed with {times} attempts!")
print("-" * 30)
print("Thanks for playing!")            
         
