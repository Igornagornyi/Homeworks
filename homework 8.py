import random
import string
from random import randint
with open('domains.txt') as file:
    lines = file.readlines()
    my_list_dl = []
    my_list_2_dl = []
for names in lines:
    my_list_dl.append(str(names[1:-1])) if str(names[-1]) == '\n' else my_list_dl.append(str(names[1:len(names)]))
number_1 = randint(0, len(my_list_dl) - 1)
number_2 = randint(0, len(my_list_dl) - 1)
number_3 = randint(0, len(my_list_dl) - 1)
my_list_2_dl.append(my_list_dl[number_1])
my_list_2_dl.append(my_list_dl[number_2])
my_list_2_dl.append(my_list_dl[number_3])

def print_random_domains():
    print(my_list_2_dl)
#############################################################################################
#2
with open('names.txt') as file:
    lines = file.readlines()
my_list_sur = []
my_list_2_sur = []
for names in lines:
    my_list_sur.append(names)
    my_list_sur = names.split()
    my_list_2_sur.append(my_list_sur[1])

def print_surnames_list():
    print(my_list_2_sur)

def print_random_surname():
    number = randint(0, len(my_list_2_sur)-1)
    em_surname = my_list_2_sur[number]
    return em_surname
################################################################################################
#3
with open('domains.txt') as file:
    lines = file.readlines()
    my_list = []
    my_list_2 = []
for names in lines:
    my_list.append(str(names[1:-1])) if str(names[-1]) == '\n' else my_list.append(str(names[1:len(names)]))
number_1 = randint(0, len(my_list) - 1)
my_list_2.append(my_list[number_1])
my_list_2 = ''.join(my_list_2)

def random_domain():
    em_domain = my_list_2
    return em_domain

def get_email_number():
    email_number = randint(100, 999)
    email_number = str(email_number)
    return email_number
def get_email_letters():
    email_letters = random.choices(string.ascii_lowercase, k=5)
    email_letters = ''.join(email_letters)
    return email_letters

def random_email():
    email_part = print_random_surname() + '.' + get_email_number() + '@' + get_email_letters() + '.' + random_domain()
    print(email_part)


random_email()
