
def filecreate():
    filexit = 0
    while int(filexit) == 0:
        filename = input("Enter the name of the file you want to create: ")
        open(filename, "w")


        userinput = input("\nCreate another file? \n[Y]    [N]\n")
        if userinput.lower() == "y":
            filexit = 0
        elif userinput.lower() == "n":
            quit()

