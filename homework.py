# www = 'www. google. com'
# if "com" in www:
#     print("com in www")
# else:
#     print("com not in www")
# www = 'www.conquer_and_command.net'
# if ".com" in www:
#     print("com in www")
# else:
#     print("not")
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
# my_indexes = [0, 1, 2, 3, 4]
# my_string = "abcde"
# for index in my_indexes:
# 	print(my_string[index])
# my_string_1 = "12"
# my_string_2 = "34"
# for symb_1 in my_string_1:
# 	for symb_2 in my_string_2:
# 		print(symb_1 + symb_2)
# my_str = 'My long string'
# l_limit = "o"
# r_limit = "g"
# my_str = list(my_str)
# sub_str = []
# sub_str.extend(my_str[5:13])
# sub_str = ''.join(sub_str)
# print(str(sub_str))
# my_list = ['ert', 'oiy', 'lgpw', 'ccbnm', 'olfg', 'ty56']
# my_list_2 = []
# for index, value in enumerate(my_list):
#     my_list_2.append(value[::-1]) if index % 2 != 0 else my_list_2.append(value)
# print(my_list_2)
my_list = ['tyiu', 'rty', 'atc', 'ty96', 'aero', 'dpl', 'avbd', 'Artep']
my_list_2 = []
for value in my_list:
    my_list_2.append(value) if value[0] == 'a' or value[0] == 'A' else None
print(my_list_2)