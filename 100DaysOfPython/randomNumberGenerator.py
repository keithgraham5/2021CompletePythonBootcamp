'''Mersenne Twister random number generator algorithm is packaged into ta random module'''
'''https://docs.python.org/3/library/random.html'''

import random

random_interger = random.randint(1, 10)#returns random whole number
print(random_interger)

random_float1 = random.random()# between 0.00 and 0.99 not including 1
random_float1 = random.random() * 5 # between 0.00 and 4.99 not including 5
print(random_float1)
print(random_float2)

random_float = random.uniform(1, 5)
print(random_float)