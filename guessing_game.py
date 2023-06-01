from datetime import datetime 
from random import randint

current_time = datetime.now()
print("\nProgram Output",current_time,'\n' + '-' * 60,'\n')

MIN_NUM = 1
MAX_NUM = 50
ALLOWED_GUESSES = 5

print(f"Guess a number between {MIN_NUM} and {MAX_NUM}. \
      You have {ALLOWED_GUESSES} guesses. Good luck!\n\n")

out_of_guesses = False
attempt_number = 1
secret_number = randint(MIN_NUM, MAX_NUM)


while not out_of_guesses:
    print(f"Enter your number for guess #{attempt_number}:")
    player_guess = int(input())

    if player_guess == 0:
        print("Quitter!")
        break

    if player_guess == secret_number and attempt_number > 1:
        print(f"Congratulations! {secret_number} was the correct number!\
              \nIt took you {attempt_number} tries to guess correctly.")
              
        out_of_guesses = True

    elif player_guess == secret_number and attempt_number == 1:
        print(f"Congratulations! {secret_number} was the correct number!\
        \nYou got it on the first try!")
        out_of_guesses = True

    elif  attempt_number == ALLOWED_GUESSES: 
        out_of_guesses = True
        print(f"You lose!!!\nThe secret number was {secret_number}")

    elif player_guess > secret_number:
        print("Guess a lower number!")
        attempt_number += 1
        
    elif player_guess < secret_number:
        print("Guess a higher number!")
        attempt_number += 1