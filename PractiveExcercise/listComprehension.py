import random
a = random.sample(range(100), 5)
print(a)
even = [evelem for evelem in a if evelem % 2 == 0]
print(even)