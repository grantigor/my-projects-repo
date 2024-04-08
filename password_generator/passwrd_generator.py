"""
# First version of random password generator

import random

upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_char = upper_char.lower()
nums = '1234567890'
spec_chars = "!@#$%^&*()_{}.,/:;"
all_chars = upper_char + lower_char + nums + spec_chars
len_pass = 15
password = ""
for i in range(len_pass):
    next_char = random.choice(all_chars)
    password = password + next_char
print(password)

# Second version

import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
password = ""
len = 15
for i in range(len):
    password += random.choice(chars)
print(password)

"""

#Third version

import random
import string

len = int(input("Enter lenght of your password: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join([random.choice(chars) for i in range(len)])
print(password)

