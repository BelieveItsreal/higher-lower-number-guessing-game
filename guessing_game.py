import random
print("Welcome! to the number guessing game!\nI am thinking of a number between 1 and 100")
number = random.randint(1, 100)
print(number)
#user input level difficulty
level = input("Choose difficulty. Type 'easy' or 'hard': ")

game_is_on = True
#for easy level
if level == "easy":
    i = 10
    while game_is_on is True and i >= 1:
        guess = int(input(f"you have {i} attempts left. Guess the number: "))
        if i == 1:
            print("\n*********You run out of moves. You lose!**********")
        elif guess < number:
            print("\nHigher")
        elif guess > number:
            print("\nlower")
        else:
            print("You Won")
        if number == guess:
            print(f"You got it right the number is {number}")
            game_is_on = False
        else:
            print("You have guessed a wrong number.")
        i = i-1

#for hard level
if level == "hard":
    i = 5
    while game_is_on is True and i >= 1:
        guess = int(input(f"you have {i} attempts left. Guess the number: "))
        if i == 1:
            print("\n*********You run out of moves. You lose!**********")
        elif guess < number:
            print("\nHigher")
        elif guess > number:
            print("\nlower")
        else:
            print("You Won")
        if number == guess:
            print(f"You got it right the number is {number}")
            game_is_on = False
        else:
            print("You have guessed a wrong number.")
        i = i-1


