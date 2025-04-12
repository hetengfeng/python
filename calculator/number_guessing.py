#!/usr/bin/env python3

import random

def get_integer_input():
    while True:
        min_value_string = input("Enter the minimum integer of your guessing range: ")
        max_value_string = input("Enter the maximum integer of your guessing range: ")
        try:
            min_value = int(min_value_string)
            max_value = int(max_value_string)
            if min_value >= max_value:
                print("The maximum is not larger than the minimum, please try again!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter two integers!")
    return min_value, max_value

def number_guessing():

        print("Welcome to Number Guessing Game!")
        print("-" * 30)
        
        min_and_max = get_integer_input()        

        times = 0

        random_number = random.randint(min_and_max[0], min_and_max[1])

        while True:
            user_input = input(f"Attempt {times +1}: ")
            try:
                guess = int(user_input)
                if guess < min_and_max[0] or guess > min_and_max[1]:
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

if __name__ == "__main__":
    number_guessing() 
