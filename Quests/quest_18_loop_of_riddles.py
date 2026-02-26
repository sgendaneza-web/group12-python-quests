secret_number = 7
guess = -1  # Start with a number that is not the secret

while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")