# a = [5, 10, 15, 20, 25]
# print(a[0])
# print(a[-1])
# print(a[2:4])
# a.append(55)
# print(a)
store = ["Milk", "Eggs", "Bread", "Meat"]
cart = []
print(store)
while True:
    try:
        iteminput = input("\nAdd item from the store: ")
    except ValueError:
        print("Item not on the list, try again")
        continue

    if iteminput in store:
        cart.append(iteminput)
        print(iteminput + " has been added to cart")
    else:
        print(iteminput + "not on the list, try again")
        continue
