my_dict = {'Valentina': 1992, 'Vadim': 2000, 'Elena': 2013, }
print('Dict:', my_dict)
print('Existing value: ', my_dict['Elena'])
print('Not existing value: ', my_dict.get('Vasilii'))
my_dict.update({'Zarina': 1990, 'Alex': 1995})
print('Deleted value: ', my_dict.pop('Vadim'))
print('Modified dictionary: :', my_dict)
print()

my_set = {15, 'фрукты', 15, 10, 'фрукты', 10, 10}
print('Set:', my_set)
my_set.add('55')
my_set.add((45, 6, 90))
my_set.discard(15)

print('Modified set:', my_set)