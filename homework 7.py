#1
import random
from random import randint
# value = randint(1, 20)
# rand_list = [randint(1, 100) for i in range(value)]
# print(value)
# print(rand_list)
###############################################################################################
#2
point_A = [randint(1, 20) for i in range(2)]
point_B = [randint(1, 20) for i in range(2)]
point_C = [randint(1, 20) for i in range(2)]
triangle = {'A': point_A, 'B': point_B, 'C': point_C}
print(triangle)