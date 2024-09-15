import random

for _ in range(10):
    print(random.randint(10, 12), end = " ")

print()
print(random.randint(100, 1000))

choice: int = random.randint(1, 2)
if choice == 1:
    print(True)
else:
    print(False)

#                                                       1     2      3    4
print("random.choice([True, False]): ", random.choice( [True, False, [] , 2.3] ))

# random and print: a day "Sunday", "Monday" ...
day: str = random.choice( ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] )
print(f'random day is {day}')

print(f"{random.uniform(9.5, 10.7):.2f}")

print(f"integer: {random.randint(10, 20):.2f}")
print(f"{random.uniform(10.5, 20):.2f}")
# num1: int = random.randint ...
# create a random first number between 0-100
# create a random second number between 0-100
# {number1} + {number2} = ?
# 30 + 70 = ?
# 100
# correct
# 90
# wrong ...

num1: int = random.randint(0, 100)
num2: int = random.randint(0, 100)
sum_num: int = num1 + num2
answer = int(input(f"{num1} + {num2} = ?"))
if answer != sum_num:
    print('wrong...')
else:
    print('correct!')

# extra -- loop
num1: int = random.randint(0, 100)
num2: int = random.randint(0, 100)
sum_num: int = num1 + num2
answer: int = int(input(f"{num1} + {num2} = ?"))
while answer != sum_num:
    print('wrong...')
    answer = int(input(f"{num1} + {num2} = ?"))
else:
    print('correct!')


