#1
my_list = ['ert', 'oiy', 'lgpw', 'ccbnm', 'olfg', 'ty56']
my_list_2 = []
for index, value in enumerate(my_list):
    my_list_2.append(value[::-1]) if index % 2 != 0 else my_list_2.append(value)
print(my_list_2)
####################################################################################
#2
my_list = ['tyiu', 'rty', 'atc', 'ty96', 'aero', 'dpl', 'avbd', 'Artep']
my_list_2 = []
for value in my_list:
    my_list_2.append(value) if value[0] == 'a' or value[0] == 'A' else None
print(my_list_2)