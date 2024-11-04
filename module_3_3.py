def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [False, '"Высшее число"', 55]
values_dict = {'a': '1', 'b': '2', 'c': '3'}

values_list_2 = [54.32, 'Строка']
print_params()
print_params(1, 2, 3)
print_params(True)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)