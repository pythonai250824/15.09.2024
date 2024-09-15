import random
# input 5 height from the user
#for _ in range(1, 5 + 1):
# sum_heights: float = 0.0
# for _ in range(1, 5 + 1):  # 0 1 2 3 4
#     # input height , until the height is between 0.4-2.5
#     height: float = float(input('enter height: '))
#     while not 0.4 <= height <= 2.5:
#         height = float(input('enter height: '))
#     else:
#         print(f"{height} is correct.")
#     sum_heights += height
#
# print(f"average = {sum_heights / 5}")
#
# """
# 1: 12345
# 2: 12345
# 3: 12345
# """
# for i in range(3):
#     for i in range(1, 5 + 1):
#         print(i, end = " ")
#     print()

#4
# * * * *
# * * * *
# * * * *
# * * * *

#4
#i=1 *
#i=2 * *
#i=3 * * *
#i=4 * * * *
for i in range(1, 4 + 1):
    #print('* ' * i)
    for _ in range(1, i + 1):
        print('*', end = " ")


