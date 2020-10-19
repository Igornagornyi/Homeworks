#express

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
            my_dict = {'folders': folders, 'files': files}
    return my_dict



# print(get_path_to_files_and_folders('D:\PycharmProjects\projects'))




#1
def read_name_date_lines(file_path):
    my_list_name = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "death" in line.lower() or "birth" in line.lower():
                my_list_name.append(line)
    return my_list_name
##############################################################################################
#2
def read_dates(path_file):
    my_list_date = []
    with open(path_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "death" in line.lower() or "birth" in line.lower():
                r_limit = line.find('-')
                my_list_date.append(line[0:r_limit].strip())
                for index in range(len(my_list_date)):
                    if 'January' in line:
                        my_list_date[index] = my_list_date[index].replace('January', '01')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'February' in line:
                        my_list_date[index] = my_list_date[index].replace('February', '02')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'March' in line:
                        my_list_date[index] = my_list_date[index].replace('March', '03')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'April' in line:
                        my_list_date[index] = my_list_date[index].replace('April', '04')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'May' in line:
                        my_list_date[index] = my_list_date[index].replace('May', '05')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'June' in line:
                        my_list_date[index] = my_list_date[index].replace('June', '06')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'July' in line:
                        my_list_date[index] = my_list_date[index].replace('July', '07')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'August' in line:
                        my_list_date[index] = my_list_date[index].replace('August', '08')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'September' in line:
                        my_list_date[index] = my_list_date[index].replace('September', '09')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'October' in line:
                        my_list_date[index] = my_list_date[index].replace('October', '10')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'November' in line:
                        my_list_date[index] = my_list_date[index].replace('November', '11')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'December' in line:
                        my_list_date[index] = my_list_date[index].replace('December', '12')
                        my_list_date[index] = my_list_date[index].split()
                        my_list_date[index] = '/'.join(my_list_date[index])
                    if 'rd' in my_list_date[index]:
                        my_list_date[index] = my_list_date[index].replace('rd', '')
                    if 'st' in my_list_date[index]:
                        my_list_date[index] = my_list_date[index].replace('st', '')
                    if 'nd' in my_list_date[index]:
                        my_list_date[index] = my_list_date[index].replace('nd', '')
                    if 'th' in my_list_date[index]:
                        my_list_date[index] = my_list_date[index].replace('th', '')
    return my_list_date

def read_names(file_path):
    my_list_name = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "death" in line.lower() or "birth" in line.lower():
                if "'" in line:
                    l_limit = line.find('-')
                    r_limit = line.find("'")
                    my_list_name.append(line[l_limit+1:r_limit].strip())
    return my_list_name


def read_name_and_date(line:str):
    # l_limit = line.find('-')
    # r_limit = line.find("'")
    # r_limit = l_limit
    # name = line[l_limit + 1:r_limit].strip()
    # date = line[:r_limit].strip()
    name = read_names('authors.txt')
    date = read_dates('authors.txt')
    my_dict = {"name": name, "date": date}
    return my_dict
##########################################################################################################################
#3

lines = read_name_date_lines('authors.txt')
def get_person_list(lines):
    result_list = []
    for line in lines:
        result_list.append(read_name_and_date(line))
        return result_list
#########################################################################################################
#4
path_file = 'authors.txt'
def read_persons_date_of_birth_and_death(path_file):
    b_date = []
    d_date = []
    name = read_names(path_file)
    with open(path_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "death" in line.lower():
                r_limit = line.find('-')
                d_date.append(line[0:r_limit].strip())
                if "birth" in line.lower():
                    b_date.append(line[0:r_limit].strip())
                    for index in range(len(d_date)):
                        if 'January' in line:
                            d_date[index] = d_date[index].replace('January', '01')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'February' in line:
                            d_date[index] = d_date[index].replace('February', '02')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'March' in line:
                            d_date[index] = d_date[index].replace('March', '03')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'April' in line:
                            d_date[index] = d_date[index].replace('April', '04')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'May' in line:
                            d_date[index] = d_date[index].replace('May', '05')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'June' in line:
                            d_date[index] = d_date[index].replace('June', '06')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'July' in line:
                            d_date[index] = d_date[index].replace('July', '07')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'August' in line:
                            d_date[index] = d_date[index].replace('August', '08')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'September' in line:
                            d_date[index] = d_date[index].replace('September', '09')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'October' in line:
                            d_date[index] = d_date[index].replace('October', '10')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'November' in line:
                            d_date[index] = d_date[index].replace('November', '11')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'December' in line:
                            d_date[index] = d_date[index].replace('December', '12')
                            d_date[index] = d_date[index].split()
                            d_date[index] = '/'.join(d_date[index])
                        if 'rd' in d_date[index]:
                            d_date[index] = d_date[index].replace('rd', '')
                        if 'st' in d_date[index]:
                            d_date[index] = d_date[index].replace('st', '')
                        if 'nd' in d_date[index]:
                            d_date[index] = d_date[index].replace('nd', '')
                        if 'th' in d_date[index]:
                            d_date[index] = d_date[index].replace('th', '')
                            for index in range(len(b_date)):
                                if 'January' in line:
                                    b_date[index] = b_date[index].replace('January', '01')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'February' in line:
                                    b_date[index] = b_date[index].replace('February', '02')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'March' in line:
                                    b_date[index] = b_date[index].replace('March', '03')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'April' in line:
                                    b_date[index] = b_date[index].replace('April', '04')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'May' in line:
                                    b_date[index] = b_date[index].replace('May', '05')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'June' in line:
                                    b_date[index] = b_date[index].replace('June', '06')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'July' in line:
                                    b_date[index] = b_date[index].replace('July', '07')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'August' in line:
                                    b_date[index] = b_date[index].replace('August', '08')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'September' in line:
                                    b_date[index] = b_date[index].replace('September', '09')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'October' in line:
                                    b_date[index] = b_date[index].replace('October', '10')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'November' in line:
                                    b_date[index] = b_date[index].replace('November', '11')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'December' in line:
                                    b_date[index] = b_date[index].replace('December', '12')
                                    b_date[index] = b_date[index].split()
                                    b_date[index] = '/'.join(b_date[index])
                                if 'rd' in b_date[index]:
                                    b_date[index] = b_date[index].replace('rd', '')
                                if 'st' in d_date[index]:
                                    b_date[index] = b_date[index].replace('st', '')
                                if 'nd' in d_date[index]:
                                    b_date[index] = b_date[index].replace('nd', '')
                                if 'th' in d_date[index]:
                                    b_date[index] = b_date[index].replace('th', '')
                                new_dict = {'name': name, 'b_date': b_date, 'd_date': d_date}
    return new_dict

