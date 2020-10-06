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
####################################################################################
#3
list_1 = ['utptr', 'cvbx', 'qqat', 'eeeouyy', 'zxcav', 'atprr']
list_2 = []
for value in list_1:
    list_2.append(value) if 'a' in value else None
print(list_2)
####################################################################################
#4
my_list = [2, 43, 57, 89, 'wer', 'rty', 'vbnb', 'df4gg', 56, 'rt5']
my_list_2 = []
for value in my_list:
    my_list_2.append(value) if value == str(value) else None
print(my_list_2)
####################################################################################
#5
my_str = 'hhhjjjjlllOPS!'
my_list = []
for i in my_str:
    my_list.append(i) if my_str.count(i) == 1 else None
print(my_list)
####################################################################################
#6
my_str = 'werty'
my_str_2 = 'qwertynbbvc'
my_str = set(my_str)
my_str_2 = set(my_str_2)
result = my_str.intersection(my_str_2)
print(result)
#####################################################################################
#7
my_str = 'QyymTmktkW'
my_str_2 = 'WrrQhhkTtkl'
my_str = list(my_str)
my_str_2 = list(my_str_2)
my_list = []
my_list_2 =[]
for i in my_str:
    my_list.append(i) if my_str.count(i) == 1 else None
for i in my_str_2:
    my_list_2.append(i) if my_str_2.count(i) == 1 else None
my_list = set(my_list)
my_list_2 = set(my_list_2)
result = my_list.intersection(my_list_2)
print(result)
########################################################################################
#8
hobby = ['traveling', 'photographing']
person_nahornyi = {'name': 'Ihor',
                   'surname': 'Nahornyi',
                   'age': 35,
                   'hobby': hobby}
residence = {'country': 'Ukraine',
              'City': 'Dnipro',
              'street': 'Panykahy',
              'building': 75}

job = {'company': 'UkSatse',
        'position': 'ATC'}
hillel_students = {'Nahornyi': person_nahornyi,
                   'Anrey': {},
                  'Kiril': {}}
print(hillel_students['Nahornyi'])
#########################################################################################
#9
cake = {'wheat': '500g',
        'milk': '1L',
        'butter': '200g',
        'eggs': 10}
cream = {'sugar': '200g',
         'sour cream': '250g',
         'vanilla': '100g',
         'butter': '150g'}
glaze = {'cocoa': '300g',
         'sugar': '100g',
         'butter': '100g'}
print('Для приготовления коржа берем следующие ингредиенты:', cake)
print('Далее готовим крем:', cream)
print('В конце покрываем глазурью:', glaze)