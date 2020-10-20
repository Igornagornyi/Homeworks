import os
import json
import csv
import random
from random import randint
import string
def random_str_with_symbols():
    random_str = string.ascii_lowercase + string.ascii_uppercase + '' + string.digits + '' + string.punctuation
    ran_size = randint(100, 1000)
    return ''.join((random.choice(random_str) + '\n\n\n\n\n\n\n\n\n') for x in range(ran_size))
file_path = str()
def write_file_txt(file_path:str):
    with open(file_path, 'w') as file:
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

file_path_2 = str()
def write_json(file_path_2:str):
    with open(file_path_2, 'w') as write_file:
        json.dump(write_text_for_json(), write_file)

###############################################################################################################
#3
file_path_3 = str()
def write_csv(file_path_3:str):
    with open(file_path_3, 'w') as csvfile:
        n_number = [0, 1]
        n_number_csv = [random.choices(n_number, k=randint(3, 10))]
        m_number = [0, 1]
        m_number_csv = [random.choices(m_number, k=randint(3, 10))]
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(n_number_csv)
        csvwriter.writerows(m_number_csv)
#################################################################################################################
#4
file_path_4 = str()
def file_writer(file_path_4:str):
    extension = file_path_4.rsplit(".")[-1]
    if extension == 'txt':
        data = write_file_txt(file_path_4)
    elif extension == 'csv':
        data = write_csv(file_path_4)
    elif extension == 'json':
        data = write_json(file_path_4)
    else:
        raise Exception('Unsupported file format')
    return data






