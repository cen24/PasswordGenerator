# Generate a random password with 4 numbers, letters and special characters each.

import string
import random


def generate_key(num):
    passwordnum = ''

    for n in range(num):
        n = random.randint(0, 9)
        passwordnum += string.printable[n]
    return passwordnum


def generate_key2(num):
    passwordletters = ''

    for n in range(num):
        l = random.randint(10, 62)
        passwordletters += string.printable[l]
    return passwordletters


def generate_key3(num):
    passwordsc = ''

    for n in range(num):
        sc = random.randint(63, 93)
        passwordsc += string.printable[sc]
    return passwordsc

#remember to remove spaces
print ("Your new password is:",generate_key(4),generate_key2(4),generate_key3(4))
