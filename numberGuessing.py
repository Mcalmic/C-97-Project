import random

randomNum = random.randint(1, 10)
guesses = 5 

while guesses > 0:
    guess = int(input("Enter your Guess between 1-10" ))
    if guess < 1 or guess > 10:
        print("Enter a number between 1-10. ")
    elif guess > randomNum:
        print("Your guess is too big.")
        guesses -= 1
    elif guess < randomNum:
        print("Your guess is too small.")
        guesses -= 1
    else:
        print("Great job! You guessed the number!")
        guesses = 0