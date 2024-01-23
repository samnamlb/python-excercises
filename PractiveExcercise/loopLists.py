list = [9, 10, 8, 7, 5, 4, 12, 3345, 484, 904]
print(len(list))
for remval in list:
     if remval % 2 != 0:
         list.remove(remval)

print(list)
print(len(list))


# nums = [2,7,11,15]
# target = 9
# formula = nums[0] + nums[1]
# if formula == target:
#     print(formula)

# with open('test_file.txt', "w") as open_file:
#     open_file.write('This was written in Python')
