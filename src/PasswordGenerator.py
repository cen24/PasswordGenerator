#Generate a random password with 12 characters.

import string
import random

def generate_key(num):
    password=''


    for n in range(num):
        r = random.randint(0,84)
        password += string.printable[r]

    return password

print ("Your new password is:", generate_key(12))
