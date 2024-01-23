with open('test_file.txt', 'r') as primelist:
    primenumbers = primelist.read()

with open('happynum.txt', 'r') as happylist:
    happynumbers = happylist.read()

commonumbers = []

for common in happynumbers:
    if common in primenumbers:
        commonumbers.append(common)

print(commonumbers)