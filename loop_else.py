#
# PIE: float = 3.14  # const
# tries = 1
# user_attempt: float = float(input('what is pie?'))
# while user_attempt != PIE:
#     # 1
#     print('wrong ...')
#     tries += 1
#     if tries > 3:
#         print('you were wrong too many times!! goodbye...')
#         break
#     user_attempt = float(input('try again, what is pie?'))
# else:
#     # 2
#     # break did NOT happend
#     print(f'correct, pie is {PIE}')
#
# # the lucky number is 777
# # input number from the user until the user guessed the number
# # count how many times the user tried
# # if the user gave the number 0 break
# # if the user guessed correctly , print "well done! , {tries}..."
#
# ########## no input before
# LUCKY_NUMBER: int = 777
# x: int = 0
# attempts: int = 0
# while x != LUCKY_NUMBER:
#     attempts += 1
#     x = int(input('guess a number'))
#     if x == 0:
#         break
# else:
# #if x == 777:
#     # he guessed 777
#     print(f"good guess. attempts = {attempts}")
#
# ########### input before
# LUCKY_NUMBER: int = 777
# x: int = int(input('guess a number'))
# attempts: int = 1
# while x != LUCKY_NUMBER:
#     # 1
#     if x == 0:
#         break
#     attempts += 1
#     x = int(input('wrong. guess again'))
# else:
#     # 2
#     #if x == 777:
#     # he guessed 777
#     print(f"good guess. attempts = {attempts}")
#
# while True:
#     #x
#     #y
#     #z
#     #avg
#     #if 0 <= x <= 10 ....
#         #break
#     pass

# input 3 grades from the user in a for-loop
# sum all of the numbers
# after that print the average
# if the user gave a number not bewteen 0-100 break (and do not print the avg)
sum_grades: int = 0
# range(1, 3 + 1, 1) : 1 2 3
# range(0, 3, 1) : 0 1 2
# range(0, 3) : 0 1 2
# range(3) : 0 1 2
for _ in range(3):
    grade = int(input('enter grade [0-100]: '))
    if not 0 <= grade <= 100:
        break
    sum_grades += grade
else:
    # not break
    avg = sum_grades / 3
    print(f"average = {avg: .2f}")



