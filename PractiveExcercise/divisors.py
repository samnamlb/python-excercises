div = int(input("Please enter a number to divide by: "))
x = list(range(1, div+1))
divisorList = []
for elem in x:
    if div % elem ==0:
        divisorList.append(elem)
print(divisorList)
