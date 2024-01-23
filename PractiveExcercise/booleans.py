# points = []
# print("9 < _")
# in_num = int(input(("What should be used to make this statement true?\n")))
#
# if 9 < in_num:
#     print("That is correct")
#     points.append(1)
# else:
#     print("That is not correct")
#
# print(points)

package = ['cola', 'pepsi', 'sprite', 'fanta', 'tsk']

for sodas in package:
    if sodas == 'tsk':
        print(sodas.upper())
    else:
        print(sodas.capitalize())