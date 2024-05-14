import random

while True:
    level = input("Level: ")
    try:
        level = int(level)
        if level>0:
            break
        else:
            pass
    except ValueError:
        pass



to_find = random.randint(1, level)

while True:
    guess = input("Guess: ")
    try:
        guess = int(guess)
    except ValueError:
        pass
    else:
        if guess<to_find:
            print("Too small!")
        elif guess>to_find:
            print("Too large!")
        else:
            print("Just right!")
            break
