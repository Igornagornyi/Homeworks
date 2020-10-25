import json
import re

#1
file_path = 'D:/PycharmProjects/projects/data.json'
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data


my_list = read_json(file_path)

#2
def list_names(tmp_str):
    names_str = tmp_str['name']
    reg_ex = r"[A-z]+"
    result = re.findall(reg_ex, names_str)
    value = result[-1]
    return len(value)

def sort_names_dict(my_list):
    sort_list = sorted(my_list, key=list_names)
    return sort_list
print(sort_names_dict(my_list))
#3
def sort_years(tmp_str):
    years_str = tmp_str['years']
    reg_ex = r"[0-9]{1,4}"
    result = re.findall(reg_ex, years_str)
    value = int(result[-1])
    value = -value if "BC" in years_str else value
    return value


def death_years_dict(my_list):
    data = sorted(my_list, key=sort_years)
    return data


#4

def sort_text(tmp_str):
    text_str = tmp_str['text']
    reg_ex = r"[A-z]"
    result = re.findall(reg_ex, text_str)
    return len(result)

def text_dict(my_list):
    data = sorted(my_list, key=sort_text)
    return data
print(text_dict(my_list))
############################################################################################################################3