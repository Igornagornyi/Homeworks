import random
import numpy
import json
import os
import string
def create_randome_triangle():
    A = numpy.random.uniform(-100.0, 100.0, 2)
    B = numpy.random.uniform(-100.0, 100.0, 2)
    C = numpy.random.uniform(-100.0, 100.0, 2)
    diff_1 = A - C
    diff_2 = B - C
    value = diff_2[-1], diff_2[0]
    mult = diff_1 * value
    result = (mult[0] - mult[1])
    square = abs(result / 2)
    if square < 0.001:
        print('Точки лежат на одной прямой')
    else:
        print('Точки не лежат на одной прямой')
    return f"{square:.{2}f}"
print(create_randome_triangle())
################################################
A = (17.0, 7.2)
def create_right_triangle(vert: A) :
    triangle_side = 200 ** 0.5
    f_num = f"{triangle_side:.{2}f}"
    B = ((A[0] + float(f_num)), A[1])
    C = (A[0], float(f_num) + A[1])
    return {'Координаты B': tuple(B), 'Координаты C': tuple(C)}
##################################################
A = (9, 12.9)
B = (12, 3.0)
C = (1.2, 0.5)
def create_triangle_with_coord(coord:tuple):
    diff_1 = (A[0] - C[0], A[1] - C[1])
    diff_2 = (B[0] - C[0], B[1] - C[1])
    value = (diff_2[-1], diff_2[0])
    mult = (diff_1[0] * value[0], diff_1[1] * value[1])
    result = mult[0] - mult[1]
    square = abs(result / 2)
    return f"{square:.{2}f}"
print(create_triangle_with_coord(coord=(A,B,C)))
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
ran_int = random.randint(4, 400)
symbol_1 = filename[0]
symbol_2 = filename[1]
symbol_3 = filename[2]
symbol_4 = filename[3]
xmin_1 = 0 if symbol_1.isdigit() else None
xmax_1 = ran_int // 4 if symbol_1.isdigit() else None
xmin_2 = ran_int // 4 if symbol_2.isdigit() else None
xmax_2 = ran_int // 2 if symbol_2.isdigit() else None
xmin_3 = ran_int // 2 if symbol_3.isdigit() else None
xmax_3 = ran_int - (ran_int // 4) if symbol_3.isdigit() else None
xmin_4 = ran_int - (ran_int // 4) if symbol_4.isdigit() else None
xmax_4 = ran_int if symbol_4.isdigit() else None
my_data = {"filename": filename, "Width": ran_int, "objects":
    {"object_1": {"class": symbol_1, "xmin": xmin_1, "xmax": xmax_1},
     "object_2": {"class": symbol_2, "xmin": xmin_2, "xmax": xmax_2},
     "object_3": {"class": symbol_3, "xmin": xmin_3, "xmax": xmax_3},
     "object_4": {"class": symbol_4, "xmin": xmin_4, "xmax": xmax_4}}}



filename = 'D:/PycharmProjects/projects/tmp_folder' + '/' + filename + '.json'
with open(filename, 'w') as json_file:
    json.dump(my_data, json_file)

    #gg
