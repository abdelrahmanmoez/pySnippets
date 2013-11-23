'''
@author: Abdelrahman Moez - aka Hydra
@script: random_generator.py
@description: This snippet generates a random combination of uppercase,
              lowercase characters and 0-9 digits, according to a given length.
@python version: 2.7
'''

import string 
import random


def generator(length):
    random_string = '' # generated random string holder
    for x in xrange(length): # generating random chr according to given length
        # combination to pick from, which contains uppercase & lowercase chars
        # and digits from 0-9
        combination = string.ascii_uppercase + string.digits + string.ascii_lowercase
        # for each step in the loop, add a random picked chr
        random_string += ''.join(random.choice(combination))
    return random_string
#
print generator(10)
