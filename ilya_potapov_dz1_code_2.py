cube = [x**3 for x in range(1,1000,2) if x % 2 != 0]
print('Cоздан список кубов нечётных чисел {}'.format(cube))
number_sum = 0
number_sum_list = []

for i in range(len(cube)):
    my_str = str(cube[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
