print("Prime or not?")


def input_prime():
    return int(input("Please enter an number: "))

numin = input_prime()
if numin % 2 == 0:
    print(numin, 'is not a prime number')
else:
    print(numin, "is a prime number")
