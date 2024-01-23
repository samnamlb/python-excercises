def a():
    print("fintion a")

def b():
    print("fintion b")

def test1():
    print("10 + 5 = ?")
    answer = int(input())
    print("Your answer is " + str(answer))
    num1 = 10
    num2 = 5
    result = num1 + num2
    if result == answer:
        print("That is correct")
    else:
        print("That is incorrect.")



def listDuplicates():
    print("Function: listDuplicates")
    a = [2, 4, 2, 6, 9, 6, 10, 20, 35, 41, 30, 6, 10, 12, 35]
    b = []
    for remove in a:
        if remove not in b:
            b.append(remove)

    print(b)

def setDuplicates(c):
        return list(set(c))
        d = [2, 4, 2, 6, 9, 6, 10, 20, 35, 41, 30, 6, 10, 12, 35]
        print(d)

def reverseWord():
    original = str(input("Please enter a string: "))
    split = original.split()
    rev = split[::-1]
    new = " ".join(rev)
    print(new)

if __name__ == '__main__':

    reverseWord()