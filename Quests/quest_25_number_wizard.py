secret_number = 10
guess = int(input("Guess my secret number: "))

if guess == secret_number:
    print("Correct!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Too low!")        
