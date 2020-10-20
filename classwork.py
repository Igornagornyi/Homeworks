# value = input("Введите число:")
# try:
#     value = float(value)
# except:
#     print('не корректный ввод')
#     value = 0.0
# print(value)
# if  value != 0:
#    result = 1 / value
# else:
#     result = "на ноль нельзя"
# print(result)

# value = None
# try:
#     value = float(value)
#     result = 1 /value
#     print(result)
# except (ValueError, ZeroDivisionError):
#     print('Что-то не так')
#     result = None
# print(result)
# except ZeroDivisionError:
#    print("Нельзя")
#    result = 0.0
# Кортежи
# tuple_1 = (1, 2, 3, 4, 'sdf')
# tuple_2 = (4, 6)
# tuple_3 = (tuple_1, tuple_2)
# print(tuple_1, type(tuple_1), len(tuple_1))
# print(tuple_2[10])
# print(tuple_3)
# for value in tuple_1[2:-1]:
#     print(value)
# a = 5
# b = 7
# (a, b) = (b ,a)
# print(a, b)
# распаковка кортежей
# val_1, val_2 = tuple_2
# print(val_1, val_2)
# val_1, _, _, _, _  = tuple_1
# print(val_1)


# Список - list
# list_1 = [1, 3, '4', 6]
# list_2 = [5, 7]
# list_3 = [list_1, list_2]
# list_2[1] = 100
# print(list_1, type(list_1), len((list_1)))
# print(list_2[1])
# print(list_3)
# list_1 .append(list_2)
# list_1 .append('list_2')
# list_1 .pop()
# print(list_1)
# my_str_list = []
# for value in list_1:
#     value = str(value)
#     my_str_list .append(value)
# print(my_str_list)
# result_str = '' .join(my_str_list)
# print(result_str)
# Пример решения задачи с месяцами
# if value in ['01', '02', '03', 'январь']:
#     print('31')
# elif value in ['04, '06']:
#     print('30')

# my_str = 'blablacar'
# my_symbol = 'bla'
# count = my_str.count(my_symbol)
#1
# text_symbol = my_symbol + '\n'
# text = my_symbol * count
# text = text.strip()
#2
# text_list = [my_symbol] * count
# text = '\n'.join(text_list)
# print(text)
#
# for index in range (count):
#     print(my_symbol)
# print('______________')
#3
# my_str = 'bla BLA car'
# lower_str = my_str.lower()
# unique_str = ''
# for i in lower_str:
#     if i not in unique_str:
#         unique_str += i
# print(len(unique_str))
#4
#5
# my_list = []
# my_str = 'qwerty'
# str_index = [0, 5, 3, 3, 4]
# for i in str_index:
#     symbol = my_str[i]
#     my_list.append(symbol)
# print(my_list)
# number = 746527310
# my_list = str(number)[::-1]
# print(int(my_list))
# my_str = "qwerty"
# my_list = []
# Решение через приведение типов
# my_list = list(my_str[::2])
# my_list.extend(list(my_str[::2]))
# print(my_list)
# решение через цикл
# my_list = [3, 5, -6]
# my_list.sort()
# print(my_list)

# Сортировка копии списка
# number = 746527310
# numb_list = list(str(number))
# numb_list.sort(reverse=True)
# str_numb = ''.join(numb_list)
# new_numb = int(str_numb)
# print(str_numb)
# my_list = [1, 20, 34, 12, -8]
# Возвести в кв элем на четн местах,а ост ост без изм
# for index in range(len(my_list)):
#     if index % 2 == 0:
#         print(my_list[index] ** 2 )
#     else:
#         print(my_list[index])
# for index, value in enumerate(my_list):
#     if index %  2 == 0:
#         print(value ** 2)
#     else:
#         print(value)
# for index, value in enumerate(my_list):
#     print(value ** index)
#  В new_list поместить числ знач из my_list, учит, что числа могут быть строкой
# my_list = [1, 2, 2, 3, 3,'4', '5', 6, 7, 'qwe', '88']
# new_list = []
# for value in my_list:
#     try:
#         value = int(value)
#         new_list.append(value)
#     except ValueError:
#         pass
# for value in my_list:
#     if type(value) == str:
#         if value.isdigit():
#             value = int(value)
#             new_list.append(value)
#         else:
#             new_list.append(value)

# print(new_list)
#  Множество Set
# Колич уник симв
# my_str = 'ggjfjjfJJHH'
# print(len(set(my_str.lower())))
# 1
# my_set_1 = {1, 2, 3, 8, 7}
# my_set_2 = {2, 3, 8, 4}
# inter = my_set_1.intersection(my_set_2)
# two_inter = inter
# my_set_1.add(7)
# print(inter, my_set_1, inter is two_inter)
# 2

# my_set_1.intersection_update(my_set_2)
# print(my_set_1)
# 3
# union = my_set_1.union(my_set_2)
# print(union)
# 4
# my_set_1.update(my_set_2)
# print(my_set_1)
# 5
# dif = my_set_1.difference(my_set_2)
# print(dif)
# 7
# sym_dif = my_set_1.symmetric_difference(my_set_2)
# print(sym_dif)
# 8
# my_set_1.symmetric_difference_update(my_set_2)
# print(my_set_1)
#
# my_str = ''
# index_a = ord('Z')
# print(index_a, chr(index_a -1))
# for index in range(ord('a'), ord('Z') + 1):
#     my_alphabet += chr(index)
# print(my_alphabet)
# Генератор списков
# my_list = [1, 2, -3, 4, -5]
# my_sqr = [value ** 2 for value in my_list if value > 0]
# print(my_sqr)
#  [print(value ** 2) for value in my_list]
# Знакомство со словарями
# childrens = ["Nastya", "Vlada", "Matvey"]
#
#
# person_zontov = {"name": "Vava",
#           "age": 41,
#           "childrens": childrens,
#           "teacher": True,
#                  12: "key_12"}
#
# math_dict = {0: "Четное число",
#              1: "Нечетное число"}
#
# hillel_teachers = {"Zontov": person_zontov,
#                    "Kaminsky": {}}

# print(math_dict[123%2])
#######################################################################
# import random
# from random import randint
# def get_rand_0_225():
#     return randint(0, 255)
# def get_ip():
#     ip_parts = [str(get_rand_0_225()) for _ in range(4)]
#     return ".".join(ip_parts)
# def sort_ip_key(ip):
#     ip_parts = [int(part) for part in ip.split(".")]
#     return ip_parts
#
# def generate_list_ip_adress(number: int, repeat = True, sort=False) -> list:
#     ip_list = []
#     for _ in range(number):
#         ip_list.append(get_ip())
#     if not repeat:
#         pass
#     if sort:
#         ip_list.sort(key=sort_ip_key)
#         return ip_list
#     else:
#         ip_list = list(set(ip_list))
#     return ip_list
# open_file = open("homework 7.py")
# for line in open_file.readlines():
#     print('***')
#     print(line)
#     print('***')
# open_file.close()
# with open("homework 7.py") as open_file:
#     for line in open_file.readlines():
#      print('***')
#      print(line)
#      print('***')
# print('Finish')


import time
import sys
# def factorial(number):
#     result = 1
#     for i in range(1, number + 1):
#         result *= i
#     return result
#
# # def write_file(filename:str, data:str):
# print(factorial(6))
import datetime
data = datetime.datetime.strptime('January', '%B')
print(data)






