import os
import random
from random import randint
import string
def random_str_with_symbols():
    random_str = string.ascii_lowercase + string.ascii_uppercase + \
                 '\n\n\n\n\n\n\n\n\n' + string.digits + string.punctuation
    ran_size = randint(100, 1000)
    return ''.join(random.choice(random_str) for x in range(ran_size))
def write_file_txt():
    with open('str.txt', 'w') as file:
        for line in random_str_with_symbols():
            file.write(random_str_with_symbols())
write_file_txt()