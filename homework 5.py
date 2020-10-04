#1
value = 1000000000000067685
value = str(value)
my_value = value.count('0')
print(int(my_value))
# ####################################################################
# #2
my_list = []
value = 30500060006
my_value = list(str(value)[::-1])
for i in my_value:
    if int(i) == 0:
        my_list.append(i)
    else:
         break
print(len(my_list))
# ####################################################################
# #3
my_list_1 = [1, 4, 5, 10, 18, 99]
my_list_2 = [34, 78, 90, 46, 75]
my_result =[]
my_result.extend((my_list_1)[0:-1:2])
my_result.extend((my_list_2)[1:-1:2])
print(my_result)
# #####################################################################
# #4
my_list = [9, 5, 7, 67, 88, 3]
new_list = []
new_list.extend((my_list)[1:len(my_list)])
new_list.extend((my_list)[:1])
print(new_list)
# ######################################################################
# #5
my_list = [2, 5, 7, 9, 33]
result = my_list.pop(0)
my_list.append(result)
print(my_list)
# ######################################################################
# #6
value = "33 44 78"
value_1 = value.split()
sum = 0
for i in value_1:
    try:
        result = int(i)
        sum += result
    except:
        pass
print(sum)
#7
value = 'asuf7pp'
value = list(value)
for i in range(0, len(value), 2):
value.insert()
value.extend('_') if len(value) % 2 != 0 else None
value_1 = []
value_2 = []
value_1.extend((value)[0:len(value):2])
value_2.extend((value)[1:len(value):2])
value_1.extend(value_2)

new_value = ''.join(new_value)[0:len(value):2]
print(value)
value_1.extend((value)[0:2])
value_1 = ''.join(value_1)
value_2.extend((value)[2:4])
value_2 = ''.join(value_2)
value_3.extend((value)[4:6])
value_3 = ''.join(value_3)
result.append(value_1)
result.append(value_2)
result.append((value_3))
print(value)
########################################################################
#8
my_str = 'My_long str'
l_limit = "o"
r_limit = "t"
my_str = list(my_str)
sub_str = []
sub_str.extend((my_str)[5:9])
sub_str = ''.join(sub_str)
print(str(sub_str))
# #########################################################################
# #9
my_str = 'My long string'
l_limit = "o"
r_limit = "g"
my_str = list(my_str)
sub_str = []
sub_str.extend((my_str)[5:13])
sub_str = ''.join(sub_str)
print(str(sub_str))
# #########################################################################
#10
list_1 = [10, 45, 18, 74, 34, 24, 25, 53, 44, 6, 85]
list_2 = []
for i in range(len(list_1)):
    list_2.append(list_1[i]) if list_1[i-1] < list_1[i] > list_1[i+1] else None
print(list_2)