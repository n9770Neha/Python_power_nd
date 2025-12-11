import random

def guess_number():
    secret_number = random.randint(0, 100)
    attempts = 0
    
    while True:
        guess = int(input("Guess a number between 1 to 100: "))
        attempts += 1

        if guess < secret_number:
            print("Too low, Try again")
        elif guess > secret_number:
            print("Too high, Try again")
        else:
            print(f"Congratulations! You have guessed the correct number in {attempts} attempts.")
            break

guess_number()
