import random

def game():
    ran_num = random.randint(1,100)
    
    while True:
        guess = int(input("Enter your guess: "))

        if guess == ran_num:
            print("Weldone you got it!")
            break
        elif guess > ran_num:
            print("Guess Lower!")
        elif guess < ran_num:
            print("Guess Higher")

game()
