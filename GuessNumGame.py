import random
secret_number = random.randint(1, 10)
max_attempts = 3

def welcome_messege():
    print("\nwelcome to the number guessing game!")
    print(f"you have {max_attempts} attempts to guess the correct number.")

def guess_recursive(attempt_left):
    guess = int(input("\nguess the number (between 1 and 10):"))
if guess == secret_number:
    print("congrulations! you guess the correct number!")
else:
    print(f"wrong guess. attempt left: {attempt_left-1}") 
    if attempts_left > 1:
        guess_recursive(attempts_left - 1)
    else: 
        print(f"\nsorry,you couldnt guess the number. the correct number was {secret_number}.")

welcome_messege()
guess_recursive(max_attempts)

print(f"memory adress of secret number {secret_number} is: {id(secret_number)}")
