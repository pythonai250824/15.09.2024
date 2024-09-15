PIE: float = 3.14  # const
tries = 1
user_attempt: float = float(input('what is pie?'))
while user_attempt != PIE and tries < 3:
    print('wrong ...')
    tries += 1
    user_attempt = float(input('try again, what is pie?'))

if user_attempt == PIE:
    print('Correct!!')
else:
    print(f'pie is {PIE}')

# Beer
beers_given: int = 0
while beers_given < 10:
    age: int = int(input('whats your age?'))
    if age >= 18:
        print('heres your beer')
        beers_given += 1
    else:
        print('youre too young to drink!')

