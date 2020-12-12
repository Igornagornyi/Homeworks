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
    return value

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
counter = 0
my_list_names = []
my_list_text = []
my_list_link = []
while counter <= 500:
    res = get_response(url)
    if res['quoteAuthor'] and res['quoteAuthor'] not in my_list_names:
        my_list_names.append(res['quoteAuthor'])
        my_list_text.append(res['quoteText'])
        my_list_link.append(res['quoteLink'])
    counter += 1

def url_list_names_sort(my_url):
    data = sorted(my_list_names)
    return data

file_path = 'D:/PycharmProjects/projects/new.csw'
def write_csv(file_path):
    with open('homework 11.csv', 'w') as csvfile:
        data_1 = url_list_names_sort(my_url)[0:20]
        data_2 = my_list_text[0:20]
        data_3 = my_list_link[0:20]
        my_data = [["quoteAuthor", "quoteText", "quoteLink"], [data_1, data_2, data_3]]
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(my_data)
# print(write_csv(file_path))






