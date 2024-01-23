# 10 point grade scale calculator

while True:
    try:
        score = float((input("Please enter your score between 0 - 100: \n")))
    except ValueError:
        print("Invalid input, try again...\n")
        continue

    if 90 <= score <= 100:
        print("Your score is A")
        break
    elif 80 <= score <= 89:
        print("Your score is B")
        break
    elif 70 <= score <= 79:
        print("Your score is C")
        break
    elif 60 <= score <= 69:
        print("Your score is D")
        break
    elif 0 <= score <= 59:
        print("Your score is F \nSorry buddy, you failed")
        break
    else:
        print("Sorry buddy, you need to enter numbers between 0 - 100\n")
        continue
