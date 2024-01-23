a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
numin = int(input("Please enter a number: "))
for element in a:
    if int(element) <= numin:
        b.append(element)

print(b)
