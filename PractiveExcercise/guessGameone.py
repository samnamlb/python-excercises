import random
i = random.randint(1, 9)
tries = 0
while True:
    try:
        randin = int(input("Guess the number: "))
    except ValueError:
        print("Invalid input, guess again...")
        continue


    if randin == i:
        print("Exactly right!")
        print("Tries: ", tries)
        i = random.randint(1, 9)
        continue

    elif randin > i:
        print("Too high")
        tries += 1
        continue

    elif randin < i:
        print("Too low")
        tries += 1
        continue
