# Python number guessing game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0 
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num } and {highest_num}")

while is_running:
    guess = input("Enter your guess:")

    if guess.isdigit():
        pass
    else:
        print("Invalid guess")
        print(f"Please select a number betwen {lowest_num } and {highest_num}")