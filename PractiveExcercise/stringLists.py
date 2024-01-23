def palindrome():
    palinput = str(input("PLease enter a palindrome: "))
    revin = palinput[::-1]
    revout = revin.lower()
    print(revout)
    if palinput.lower() == revout:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")