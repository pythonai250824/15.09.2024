import random

for _ in range(10):
    print(random.randint(10, 12), end = " ")

print()
print(random.randint(100, 1000))

print(f"{random.uniform(9.5, 10.7):.2f}")

print(f"integer: {random.randint(10, 20):.2f}")
print(f"{random.uniform(10.5, 20):.2f}")

