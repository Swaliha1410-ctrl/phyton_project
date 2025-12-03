# dice rolling game

import random

s=input('do you wants to roll as dice(y/n)')
while True:
    if s.lower=='y':
        print(f'you got no:-{random.randint(1,6)}')
    elif s.lower=='n':
        print('thanks for playing!!')
        break
    else:
        print('Invalid choice!')