# www = 'www. google. com'
# if "com" in www:
#     print("com in www")
# else:
#     print("com not in www")
######################################################################################
# www = 'www.conquer_and_command.net'
# if ".com" in www:
#     print("com in www")
# else:
#     print("not")
######################################################################################
# value = "123456789"
# my_str = value if len(value) <= 5 else value[2:5:2]
# print(my_str[::-1])
# my_str = "My name is Vova. I am a teacher!"
# for i in my_str:
#     if not i .isupper() and i .isalpha():
#       print(i)
# value = 0
# values = [value] * 6
# value = 1
# print(values)
# my_list = [0]
# values = [my_list.copy()] * 3
# my_list.append(1)
# print(values)
# my_list = ["a", "b", "c", "s", "r", "f"]
# my_str = "".join(my_list[::2])
# print(my_str)
# my_value = 123.45678
# my_str = f"my_value= {my_value:.3f}"
# print(my_str)
#############################################################################
# my_indexes = [0, 1, 2, 3, 4]
# my_string = "abcde"
# for index in my_indexes:
# 	print(my_string[index])
##################################################################################
# my_string_1 = "12"
# my_string_2 = "34"
# for symb_1 in my_string_1:
# 	for symb_2 in my_string_2:
# 		print(symb_1 + symb_2)
##################################################################################
# my_list = ['ert', 'oiy', 'lgpw', 'ccbnm', 'olfg', 'ty56']
# my_list_2 = []
# for index, value in enumerate(my_list):
#     my_list_2.append(value[::-1]) if index % 2 != 0 else my_list_2.append(value)
# print(my_list_2)
###################################################################################
# my_str = 'tyiu' , 'rty', 'atc', 'ty96', 'aero', 'dpl', 'avbd', 'Artep'
# my_str = ''.join(my_str)
# print(my_str.startswith('t'))
# my_list_2 = []
# for value in my_list:
#     my_list_2.append(value) if value[0] == 'a' or value[0] == 'A' else None
# print(my_list_2)
# my_list = [1, 4, 8, 10]
# print(mi(my_list))
#####################################################################################
# list_1 = [10, 45, 18, 74, 34, 24, 25, 53, 44, 6, 85]
# list_2 = []
# for i in range(len(list_1)-1):
#     list_2.append(list_1[i]) if list_1[i-1] < list_1[i] > list_1[i+1] else None
# print(list_2)
######################################################################################
# symbol_dict = dict(a=1, b=2, c=1)
#
# symbol_dict["d"] = 5
# # symbol_dict.popitem()
# # print(symbol_dict.get("d"))
# this_key = "d"
#
# if this_key in symbol_dict.keys():
#     print("--->", symbol_dict[this_key])
#
# value = symbol_dict[this_key] if this_key in symbol_dict.keys() and symbol_dict[this_key] > 1  else -100
# print("value = ", value)

import random
from random import randint
# def special_print(min_value, max_value,):
#     print("max_value: ", max_value)
#     value = randint(min_value, max_value)
#     print(f"This random value is {value}")
#     return value
# value_1 = special_print(1, 10)
# value_2 = special_print(10, 100)
# print(value_1, value_2)
# special_print(1, 20)

import random
import string
# from random import randint
# with open('domains.txt') as file:
#     lines = file.readlines()
#     my_list_dl = []
#     my_list_2_dl = []
#     my_list_dl.extend(lines)
# for names in lines:
#     my_list_dl.append(names[1:-1]) if (names[-1]) == '\n' else my_list_dl.append(names)
# number_1 = randint(0, len(my_list_dl)-1)
# number_2 = randint(0, len(my_list_dl)-1)
# number_3 = randint(0, len(my_list_dl)-1)
# my_list_2_dl.append(my_list_dl[number_1])
# my_list_2_dl.append(my_list_dl[number_2])
# my_list_2_dl.append(my_list_dl[number_3])
# print(my_list_2_dl)



