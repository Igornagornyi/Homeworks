#1
def read_dates_and_events(path_file):
    my_list = []
    with open('authors.txt', 'r') as file:
        lines = file.readlines()
        for data in lines:
            r_limit = data.find('-')
            if len(data) > 10:
                my_list.append(data[0:r_limit+1])
            if ' birthday' in data:
                my_list.append('birthday')
            elif 'death' in data:
                my_list.append('death')
            else:
                pass
    return my_list
##############################################################################################
#2
def read_dates(path_file):
    my_list_date = []
    with open('authors.txt', 'r') as file:
        lines = file.readlines()
        for data in lines:
            r_limit = data.find('-')
            if len(data) > 12 and data[r_limit-2].isdigit():
                my_list_date.append(data[0:r_limit])
            else:
                pass
        return my_list_date
def read_names(file_path):
    my_list_name = []
    with open('authors.txt', 'r') as file:
        lines = file.readlines()
        for data in lines:
            l_limit = data.find('-')
            r_limit = data.find("'")
            if len(data) > 10:
                my_list_name.append(data[l_limit+1:r_limit+1])
            else:
                pass
        return my_list_name

def read_name_and_date(name, date):
    my_dict = {"name": name, "date": date}
    return my_dict

name = read_names('authors.txt')
date = read_dates('authors.txt')




print(read_dates('authors.txt'))