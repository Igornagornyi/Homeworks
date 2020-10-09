#1
import random
from random import randint
value = randint(1, 20)
rand_list = [randint(1, 100) for i in range(value)]
print(value)
print(rand_list)
###############################################################################################
#2
point_A = [randint(1, 20) for i in range(2)]
point_B = [randint(1, 20) for i in range(2)]
point_C = [randint(1, 20) for i in range(2)]
triangle = {'A': point_A, 'B': point_B, 'C': point_C}
print(triangle)
###############################################################################################
#3
def my_print(my_str):
    my_str += '*' * 3
    my_str = my_str[::-1]
    my_str += '*' * 3
    my_str = my_str[::-1]
    print(my_str)
###############################################################################################
#4a
my_dict_1 = dict(a=1, b=2, c=100, d='qwe', i=0)
my_dict_2 = dict(b=3, f=8, e=1000, d='qwe', p=13)
my_list = []
for key in my_dict_1:
    my_list.append(key) if key in my_dict_2 else None
print(my_list)
#4б
my_dict_1 = dict(a=1, b=2, c=100, d='qwe', i=0)
my_dict_2 = dict(b=3, f=8, e=1000, d='qwe', p=13)
my_list = []
for key in my_dict_1:
    my_list.append(key) if key not in my_dict_2 else None
print(my_list)
#4в
my_dict_1 = dict(a=1, b=2, c=100, d='qwe', i=0)
my_dict_2 = dict(b=3, f=8, e=1000, d='qwe', p=13)
my_dict_3 = dict()
my_dict_1 = set(my_dict_1.items())
my_dict_2 = set(my_dict_2.items())
result = my_dict_1.difference(my_dict_2)
result = dict(result)
print(result)
#4г
my_dict_1 = dict(a=1, b=2, c=100, d='qwe', i=0)
my_dict_2 = dict(b=3, f=8, e=1000, d='qwe', p=13)
my_dict_3 = dict()
for key in my_dict_1:
    if key in my_dict_2 and my_dict_1[key] != my_dict_2[key]:
        my_dict_3[key] = (my_dict_1[key], my_dict_2[key])
    else:
        my_dict_3[key] = my_dict_1[key]
for key in my_dict_2:
    if key not in my_dict_1.keys():
        my_dict_3[key] = my_dict_2[key]
print(my_dict_3)
