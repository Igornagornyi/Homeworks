import random
import string
from random import randint

def read_domains(file_path):
    my_list_dl = []
    with open('domains.txt', 'r') as file:
        lines = file.readlines()
    for names in lines:
            my_list_dl.append(str(names[1:-1])) if str(names[-1]) == '\n' else my_list_dl.append(str(names[1:len(names)]))
    return my_list_dl

#############################################################################################
#2

def read_names(file_path):
    my_list_sur = []
    my_list_2_sur = []
    with open('names.txt', 'r') as file:
        lines = file.readlines()
    for names in lines:
        my_list_sur.append(names)
        my_list_sur = names.split()
        my_list_2_sur.append(my_list_sur[1])
    return my_list_2_sur



################################################################################################
#3

def random_name(names):
    return list(set(names))[0]


def random_domain(domains):
    return list(set(domains))[0]

def get_email_number():
    email_number = randint(100, 999)
    email_number = str(email_number)
    return email_number
def get_email_letters():
    email_letters = random.choices(string.ascii_lowercase, k=5)
    email_letters = ''.join(email_letters)
    return email_letters

def random_email(domains, names):
    email_part = random_name(names) + '.' + get_email_number() + '@' + get_email_letters() + '.' + random_domain(domains)
    return email_part

domains = read_domains('domains.txt')
names = read_names('names.txt')


