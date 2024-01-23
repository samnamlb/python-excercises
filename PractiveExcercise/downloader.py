def excerciseone():
    list1 = [1, 6, 80, 67, 44, 33, 24]
    list2 = [3, 8, 7, 10, 50, 90, 78, 56]
    list3 = []

    for even in list1:
        if even % 2 == False:
            list3.append(even)

    for odd in list2:
        if odd % 2:
            list3.append(odd)

    print(list3)

def charremove(stringinput, charinput):

    alphastring = stringinput.replace(charinput.lower(), '')
    betastring = alphastring.replace(charinput.upper(), '')

    print("New string: ", betastring)

def middleSlide(s1,s2):
    middleIndex = int(len(s1) /2)
    print("Original Strings are: ", s1, s2)
    slidebetween = s1[:middleIndex:]+ s2 +s1[:middleIndex:]
    print("After sliding new string in middle", slidebetween)

middleSlide("Sam", "Lee")