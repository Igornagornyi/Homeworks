#1
# my_list = [1, 4, 8, 127, 258, 112]
# for i in my_list:
#     if i > 100:
#       print(i)
#############################################################################################################################
#2
# my_list = [1, 4, 8, 127, 258, 112]
# my_list_2 = []
# for i in my_list:
#     my_list_2.append(i) if i > 100 else None
# print(my_list_2)
#############################################################################################################################
#3
# my_list = [1, 3, 5, 6, 10, 87, 54, 68]
# my_list.append(0) if len(my_list) < 2 else my_list.append(my_list[-1] + my_list[-2])
# print(my_list)
#############################################################################################################################
#4
# value = input('Введите число:')
# try:
#     value = float(value)
#     result = value ** (-1)
#     print(result)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except ValueError:
#     print('Неправильный ввод.')
#     print('Возможно, вы используете буквы вместо цифр или используете запятую вместо точки, при написании нецелых чисел.')
##############################################################################################################################
#5
# my_list = ['a', 'b', 'c', 'd', 'e']
# my_indexes = [0, 1, 2, 3, 4]
# for i in my_indexes:
#    print(my_list[i])
##############################################################################################################################
#6
# my_list_1 = ['a', 'b', 'c', 'd']
# my_list_2 = ['e', 'f', 'g', 'h']
# my_indexes = [0, 1, 2, 3]
# for i in my_indexes:
#     result = ','.join(my_list_1[i] + my_list_2[i])
#     print(result)
##############################################################################################################################
#7
# my_string_1 = '0123456789'
# my_list_2 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# my_list_3 = []
# for symbol_1 in my_string_1:
#     for symbol_2 in my_list_2:
#         result = (int(symbol_1) + symbol_2)
#         my_list_3.append(result)
#         my_list_3.sort()
# print(my_list_3)



