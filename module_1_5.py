immutable_var=(1, 4.5, True, 'яблоко',[1, 2])
print(immutable_var)
#immutable_var[0] = 1 -неизменяемый элемент кортежа
#immutable_var[1] = 1 -неизменяемый элемент кортежа
#immutable_var[2] = 1 -неизменяемый элемент кортежа
#immutable_var[3] = 1 -неизменяемый элемент кортежа
immutable_var[4][1] = 6 #изменяемый элемент кортежа
mutable_list=[1, 5.1, False, 'банан']
mutable_list[0] = 'квадрат'
mutable_list.extend('куб')
print(mutable_list)