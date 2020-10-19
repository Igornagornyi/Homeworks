import os
import json
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
# ####################################################################################################################
#2

def write_text_for_json():
    ran_lsize = randint(5, 10)
    my_string = string.ascii_lowercase
    my_ran_letters = [random.choices(my_string, k=5) for i in range(ran_lsize)]
    my_ran_letters = [''.join(i) for i in my_ran_letters]
    key = my_ran_letters
    ran_nsize = randint(-100, 100)
    ran_fsize = '0.' + random.choice('0123456789')
    ran_fsize = float(ran_fsize)
    random_decision = ['True', 'False']
    ran_dec = random.choice(random_decision)
    my_value = [ran_nsize, ran_fsize, ran_dec]
    value = random.choice(my_value)
    json_dict = {"key": key, "value": value}
    return json_dict


def print_json():
    with open('new.json', 'w') as write_file:
        json.dump(write_text_for_json(), write_file)
###############################################################################################################3
#3gff
