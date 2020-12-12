
import json
import csv
import random
from random import randint
import string



file_path = 'D:/PycharmProjects/projects/new.csv'
class FileWriter:
    def __init__(self, file_path):
        self.filename = file_path
        self.data = [[1, 2, 3, 4], [5, 6, 7, 8], 9, 10, 11, 12]
        self.write()



    def random_str_with_symbols(self):
        random_str = string.ascii_lowercase + string.ascii_uppercase + '' + string.digits + '' + string.punctuation
        ran_size = randint(100, 1000)
        return ''.join((random.choice(random_str) + '\n' * 9) for x in range(ran_size))


    def write_file_txt(self, data):
        with open(file_path, 'w') as file:
            if data:
                file.write(data)
            else:
                file.write(self.random_str_with_symbols())

    def write_text_for_json(self):
        ran_lsize = randint(5, 10)
        my_string = string.ascii_lowercase
        my_ran_letters = [random.choices(my_string, k=5) for i in range(ran_lsize)]
        my_ran_letters = [''.join(i) for i in my_ran_letters]
        key = my_ran_letters
        ran_nsize = randint(-100, 100)
        ran_fsize = '0.' + random.choice('0123456789')
        ran_fsize = float(ran_fsize)
        random_decision = ['True', 'False']
        ran_dec = random.choice(random_decision)
        my_value = [ran_nsize, ran_fsize, ran_dec]
        value = random.choice(my_value)
        json_dict = {"key": key, "value": value}
        return json_dict

    def write_json(self, data):
        with open(file_path, 'w') as write_file:
            if data:
                json.dump(data, write_file)
            else:
                json.dump(self.write_text_for_json(), write_file)

    def write_csv(self, data):
        with open(file_path, 'w') as csvfile:
            n_number = [0, 1]
            n_number_csv = [random.choices(n_number, k=randint(3, 10))]
            m_number = [0, 1]
            m_number_csv = [random.choices(m_number, k=randint(3, 10))]
            csvwriter = csv.writer(csvfile)
            if data:
                csvwriter.writerow(data)
            else:
                csvwriter.writerow(n_number_csv)
                csvwriter.writerows(m_number_csv)

    def write(self):
        extension = file_path.rsplit(".")[-1]
        if extension == 'txt':
            file_data = self.write_file_txt(data=self.data)
        elif extension == 'csv':
            file_data = self.write_csv(data=self.data)
        elif extension == 'json':
            file_data = self.write_json(data=self.data)
        else:
            raise Exception('Unsupported file format')
        return file_data




my_writer = FileWriter(file_path)
