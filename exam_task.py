import random
import json
import os
import string
def create_randome_triangle():
    A = (random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0))
    B = (random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0))
    C = (random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0))
    diff_1 = (A[0] - C[0]), (A[1] - C[1])
    diff_2 = (B[0] - C[0]), (B[1] - C[1])
    diff_2_rev = diff_2[-1], diff_2[0]
    mult = diff_1[0] * diff_2_rev[0], diff_1[1] * diff_2_rev[1]
    diff_3 = (mult[0] - mult[1])
    square = abs(diff_3 / 2)
    if square < 0.001:
        print('Точки лежат на одной прямой')
    else:
        print('Точки не лежат на одной прямой')
    return f"{square:.{2}f}"

################################################
A = (17.0, 7.2)
def create_right_triangle(vert: A) :
    triangle_side = 200 ** 0.5
    f_num = f"{triangle_side:.{2}f}"
    B = ((A[0] + float(f_num)), A[1])
    C = (A[0], float(f_num) + A[1])
    return {'Координаты B': tuple(B), 'Координаты C': tuple(C)}
##################################################
A = (14.3, 12.9)
B = (12, 3.0)
C = (1.2, 0.5)
def create_triangle_with_coord(coord:tuple):
    diff_1 = (A[0] - C[0], A[1] - C[1])
    diff_2 = (B[0] - C[0], B[1] - C[1])
    diff_2_rev = (diff_2[-1], diff_2[0])
    mult = (diff_1[0] * diff_2_rev[0], diff_1[1] * diff_2_rev[1])
    diff_3 = mult[0] - mult[1]
    square = abs(diff_3 / 2)
    return f"{square:.{2}f}"
##################################################################################
#2
def ran_str_six_symb():
    ran_dig = '0123456789_'
    ran_lett = random.choices(string.ascii_lowercase, k=2)
    ran_str = ''.join(random.choices(ran_dig, k=4) + ran_lett)
    return ran_str

try:
    os.mkdir('tmp_folder')
except FileExistsError:
    pass

filename = ran_str_six_symb()
def write_dict_for_json():
    my_data = {}
    my_data["filename"] = filename[0:4]
    ran_int = random.randint(4, 400)
    my_data["Width"] = ran_int
    my_data["objects"] = []
    for index, symbol in enumerate(my_data["filename"]):
        my_obj = {"object": {}}
        step = ran_int // 4
        my_obj["object"]["symbol"] = symbol
        my_obj["object"]["xmin"] = (step * index)
        my_obj["object"]["xmax"] = (step * index) + step
        if symbol != "_":
            my_data["objects"].append(my_obj)
    return my_data

my_filename = 'D:/PycharmProjects/projects/tmp_folder' + '/' + filename + '.json'
with open(my_filename, 'w') as json_file:
    json.dump(write_dict_for_json(), json_file, indent=2)


