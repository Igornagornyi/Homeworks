#express
from datetime import datetime
import os
def get_path_to_files_and_folders(path):
    files = []
    folders = []
    list_dir = os.listdir(path)
    for item in list_dir:
        path_item = os.path.join(path, item)
        if os.path.isfile(path_item):
            files.append(path_item)
        else:
            folders.append(path_item)
            my_dict_folders = {'folders': folders, 'files': files}
    return my_dict_folders
###########################################################################################################3
#1
def read_name_date_lines(file_path):
    my_list_name = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            if "death" in line.lower() or "birth" in line.lower() or 'died' in line.lower():
                my_list_name.append(line.strip())
    return my_list_name
##############################################################################################
#2
def get_date_numbers(number_line):
    return "".join([symbol for symbol in number_line if symbol.isdigit()])


def get_date(line):
    date = line.split("-")[0].strip().split()
    date = f"{get_date_numbers(date[0])} {date[1]} {date[2]}"
    res_date = datetime.strptime(date, '%d %B %Y').strftime('%d/%m/%Y')
    return res_date

def read_names(line):
    my_list_name = []
    if "death" in line.lower() or "birth" in line.lower():
        if "'" in line:
            l_limit = line.find('-')
            r_limit = line.find("'")
            my_list_name.append(line[l_limit + 1:r_limit].strip())
    if "died" in line:
            l_limit = line.find('-')
            r_limit = line.find('died')
            my_list_name.append(line[l_limit+1:r_limit].strip())
    return my_list_name

def read_name_date_dict(line):
    my_dict = {}
    my_dict["name"] = read_names(line)
    date = get_date(line)
    my_dict["date"] = date
    return my_dict if my_dict["name"] else {}
##########################################################################################################################
#3
def read_name_and_b_date_d_dict_dict(line):
    my_dict_2 = {}
    my_dict_2["name"] = read_names(line)
    date = get_date(line)
    if 'birth' in line.lower():
        my_dict_2["b_date"] = date
    elif 'death' in line.lower() or 'died' in line.lower():
        my_dict_2["d_date"] = date
    return my_dict_2 if my_dict_2["name"] else {}
print(read_name_and_b_date_d_dict_dict(line=read_name_date_lines('authors.txt')[0]))
##########################################################################################################################
#4

def get_person_name_date_dict_list(lines):
    result_list = []
    for line in lines:
        my_dict = read_name_and_b_date_d_dict_dict(line)
        if my_dict:
            result_list.append(my_dict)
    return result_list
#########################################################################################################
