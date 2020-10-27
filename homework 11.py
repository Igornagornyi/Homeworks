import json
import re
import requests
import csv

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

############################################################################################################################

url = 'https://api.forismatic.com/api/1.0/'
my_dict = {'method': 'getQuote', 'lang': 'ru', 'format': 'json'}
def get_response(url):
    response = requests.get(url, params=my_dict)
    return response.json()


my_url = get_response(url)
def url_list_names(tmp_dict):
    url_name_str = tmp_dict['quoteAuthor']
    reg_ex = r"[\/а-яА-ЯёЁA-z].+"
    result = re.findall(reg_ex, url_name_str)
    return result if my_url['quoteAuthor'] else {}


def url_list_names_dict(my_url):
    data = sorted(my_url, key=url_list_names)
    return data

def url_text_dict(my_url):
    url_text = my_url['quoteText']
    reg_ex = r"[а-яА-ЯёЁ].+"
    result = re.findall(reg_ex, url_text)
    return result if my_url['quoteAuthor'] else {}


def url_link_dict(my_url):
    url_link = my_url['quoteLink']
    reg_ex = r"(?:https?:\/\/)?.[a-z]+.[a-z]{1,3}.[a-z]{2}.[0-9a-z]+"
    result = re.findall(reg_ex, url_link)
    return result if my_url['quoteAuthor'] else {}

file_path = 'D:/PycharmProjects/projects/new.csw'
def write_csv(file_path):
    fieldnames = ['quoteAuthor', 'quoteText', 'quoteLink']
    with open('new.csv', 'w') as csvfile:
        data_1 = url_list_names(my_url)
        data_2 = url_text_dict(my_url)
        data_3 = url_link_dict(my_url)
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['quoteAuthor', 'quoteText', 'quoteLink'])
        csvwriter.writerows([data_1, data_2, data_3])




        # csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # data_1 = url_list_names_dict(my_url) in range(20)
        # data_2 = url_text_dict(my_url)
        # data_3 = url_link_dict(my_url)
        # csvwriter.writeheader
        # csvwriter.writerow({'quoteAuthor': data_1, 'quoteText': data_2, 'quoteLink': data_3})




