import random
import string
from random import randint
with open('domains.txt') as file:
    lines = file.readlines()
    my_list_dl = []
    my_list_2_dl = []
    my_list_3_dl = []
    my_list_dl.extend(lines)
for names in my_list_dl:
    my_list_2_dl.append(str(names[1:-1])) if str(names[-1]) == '\n' else my_list_2_dl.append(str(names[1:len(my_list_2_dl)]))
number_1 = randint(0, len(my_list_2_dl)-1)
number_2 = randint(0, len(my_list_2_dl)-1)
number_3 = randint(0, len(my_list_2_dl)-1)
my_list_3_dl.append(my_list_2_dl[number_1])
my_list_3_dl.append(my_list_2_dl[number_2])
my_list_3_dl.append(my_list_2_dl[number_3])
print(my_list_3_dl)


def print_random_domains():
    print(my_list_3_dl)
#############################################################################################
#2
with open('names.txt') as file:
    lines = file.readlines()
my_list_sur = []
my_list_2_sur = []
my_list_sur.extend(lines)
for names in my_list_sur:
    my_list_sur = names.split()
    my_list_2_sur.append(my_list_sur[1])

def print_surnames_list():
    print(my_list_2_sur)

def print_random_surname():
    number = randint(0, len(my_list_2_sur))
    em_surname = my_list_2_sur[number]
    return em_surname
################################################################################################
#3
with open('domains.txt') as file:
    lines = file.readlines()
    my_list = []
    my_list_2 = []
    my_list_3 = []
    my_list.extend(lines)
for names in my_list:
    my_list_2.append(str(names[1:-1])) if str(names[-1]) == '\n' else my_list_2.append(str(names[1:len(my_list_2)]))
number_1 = randint(0, len(my_list_2)-1)
my_list_3.append(my_list_2[number_1])
my_list_3 = ''.join(my_list_3)

def random_domain():
    em_domain = my_list_3
    return em_domain

def get_email_number():
    email_number = randint(100, 999)
    em_number = str(email_number)
    return em_number
def get_email_letters():
    email_letters = random.choices(string.ascii_lowercase, k=5)
    email_letters = ''.join(email_letters)
    em_letters = str(email_letters)
    return em_letters

def random_email():
    email_part = print_random_surname() + '.' + get_email_number() + '@' + get_email_letters() + '.' + random_domain()
    print(email_part)

