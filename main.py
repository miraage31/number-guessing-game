import art
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty(choice):
    if choice == "easy":
        return EASY_LEVEL
    elif choice == "hard":
        return HARD_LEVEL

def check_guess(p_guess, answer, p_lives):
    if p_guess > answer:
        print("Too high.\nTry again.")
        return p_lives - 1
    elif p_guess < answer:
        print("Too low.\nTry again.")
        return p_lives - 1
    else:
        print(f"You got it! The answer is {answer}")

def game():
    chosen_number = random.randint(1, 100)  # Number to guess
    guess = 0
    print(art.logo)
    difficulty = input("Choose a difficulty: 'easy' | 'hard'\n").lower()
    while difficulty != "easy" and difficulty != "hard":
        difficulty = input("Please type either 'easy' or 'hard'.\n").lower()
    lives = (set_difficulty(difficulty)) # Sets the lives based on the difficulty
    while guess != chosen_number:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Pick a number from 1-100: "))
        lives = check_guess(guess, chosen_number, lives)
        if lives == 0:
            print(f"The answer is: {chosen_number}")
            return
    print("Thanks for playing.")
game()