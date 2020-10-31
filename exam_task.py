import random
import numpy

def create_randome_triangle():
    A = numpy.random.uniform(-100.0, 100.0, 2)
    B = numpy.random.uniform(-100.0, 100.0, 2)
    C = numpy.random.uniform(-100.0, 100.0, 2)
    diff_1 = A - C
    diff_2 = B - C
    diff_3 = diff_2[-1], diff_2[0]
    mult = diff_1 * diff_3
    sum = 0
    for i in mult:
        sum = sum + i
        square = abs(sum / 2)
    if square < 0.001:
        print('Точки лежат на одной прямой')
    else:
        print('Точки не лежат на одной прямой')
    return f"{square:.{2}f}"

################################################
A = (10.0, 5.2)
def create_right_triangle(vert: A) :
    num = 2 ** 0.5
    f_num = f"{num:.{2}f}"
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
    diff_3 = (diff_2[-1], diff_2[0])
    mult = (diff_1[0] * diff_3[0], diff_1[1] * diff_3[1])
    sum = 0
    for i in mult:
        sum = sum + i
        square = abs(sum / 2)
    return f"{square:.{2}f}"
