secret_code = 42
attempts = 3

while attempts > 0:
    guess = int(input("Guess the secret_code: "))

    if guess == secret_code:
        print("Correct! Access granted!")
        break
    else:
        attempts -=1
        print("Wrong code! Try again!")

        if attempts > 0:
            print(f"You have {attempts} attempts left.")
        else:
            print("No attempts left!")
            print("Access denied!")    
    