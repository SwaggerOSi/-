data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
summ = 0
def calculate_structure_sum(element):
    global summ
    for i in range(len(element)):
        if isinstance(element[i], list | tuple):
            element1 = element[i]
            calculate_structure_sum(element1)
        elif isinstance(element[i], set):
            element2 = list(element[i])
            calculate_structure_sum(element2)
        elif isinstance(element[i], dict):
            element3 = list(element[i].items())
            calculate_structure_sum(element3)
        elif isinstance(element[i], str):
            summ += len(element[i])
        elif isinstance(element[i], int | float):
            summ += element[i]
    return summ

result = calculate_structure_sum(data_structure)
print(result)