#!/usr/bin/env python3

import random

def get_number_or_quit():
    while True:
        user_input = input("How many dices would you like to roll ('q' or 'quit' to quit the game): ")
        if user_input == 'q' or user_input == 'quit':
            return user_input
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Invalid input, Please enter an integer.")

def dice_rolling_simulator():
    print("------Welcome to the dice rolling simulator------")
    while True:
        results = []   
        dice_number = get_number_or_quit()
        if dice_number == 'q' or dice_number == 'quit':
            break
        for i in range(dice_number):
            random_number = random.randint(1, 6)
            results.append(random_number)
        print(f"These are the results: {results}. The total number is {sum(results)}/{6 * dice_number}.")
    print("Thanks for playing, practice makes perfect, have a good night in casino!")

if __name__ == "__main__":
    dice_rolling_simulator()

         
