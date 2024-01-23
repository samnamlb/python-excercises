
with open('test_file.txt', 'r') as open_file:
    all_text = open_file.read()
    substringD = "Darth"
    substringL = "Lea"
    substringLU = "Luke"
    countdarth = all_text.count(substringD)
    countLea = all_text.count(substringL)
    countLuke = all_text.count(substringLU)
    print("Darth:", countdarth)
    print("Lea:", countLea)
    print("Luke:", countLuke)
