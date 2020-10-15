def read_dates_and_events(path_file):
    my_list = []
    with open('authors.txt', 'r') as file:
        lines = file.readlines()
    for data in lines:
        r_limit = data.find('-')
        if len(data) > 12:
            my_list.append(data[0:r_limit+1])
            if ' birthday' in data:
                my_list.append('birthday')
            elif 'death' in data:
                my_list.append('death')
            else:
                pass
    return my_list

