'''
exercise1
Create a function that generates a random password. The password generated by the function
must have the following characteristics:
a. Length between 8 and 12 characters
b. Use at least one uppercase character, a number and a symbol. The function must be able to
generate passwords containing more than one character of these types, not just a single one
of each type.
'''

import random
import string

def create_password():
    length = random.randint(8, 12)
    password = ''
    password += random.randrange(string.ascii_uppercase)

    # defining sets of characters:
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list('!@#$%&/()=?')

    