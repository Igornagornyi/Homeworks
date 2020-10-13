import random
import string
from random import randint
with open('domains.txt') as file:
    lines = file.readlines()
for names in lines:
    my_list = []
    my_list_2 = []
    my_list_3 = []
    my_list.extend(lines)
for names in my_list:
    my_list_2.append(str(names[1:-1])) if str(names[-1]) == '\n' else my_list_2.append(str(names[1:len(my_list_2)]))
number_1 = randint(1, len(my_list_2)-1)
number_2 = randint(1, len(my_list_2)-1)
number_3 = randint(1, len(my_list_2)-1)
my_list_3.append(my_list_2[number_1])
my_list_3.append(my_list_2[number_2])
my_list_3.append(my_list_2[number_3])

def print_random_domains():
    print(my_list_3)
#############################################################################################
#2
# with open('names.txt') as file:
#     lines = file.readlines()
#     for names in lines:
#         my_list = []
#         my_list_2 = []
#         my_list.extend(lines)
#     for names in my_list:
#         my_list = names.split()
#         my_list_2.append(my_list[1])
#
# def print_surnames_list():
#     print(my_list_2)
#
# def print_random_surname():
#     number = randint(0, len(my_list_2))
#     print(my_list_2[number])
################################################################################################
#3
# with open('domains.txt') as file:
#   lines = file.readlines()
# for names in lines:
#        my_list = []
#        my_list_2 = []
#        my_list_3 = []
#        my_list.extend(lines)
# for names in my_list:
#        my_list_2.append(str(names[1:-1])) if str(names[-1]) == '\n' else my_list_2.append(str(names[1:len(my_list_2)]))
# number_1 = randint(0, len(my_list_2)-1)
# my_list_3.append(my_list_2[number_1])
# my_list_3 = str(my_list_3)
# print(my_list_3)

def get_email_number():
    email_number = randint(100, 999)
    print(str(email_number))
def get_email_letters():
    email_letters = random.choices(string.ascii_lowercase, k=5)
    email_letters = ''.join(email_letters)
    print(str(email_letters))

print_random_domains()