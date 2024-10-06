immutable_var = 650, 'speed', "Dule", 'language'
print(type(immutable_var))
print(immutable_var)
#immutable_var[1] = 18
#print(immutable_var) Кортеж ругается на неверный синтаксис.
tuple_ =650, 'speed', "Dule", 'language'
print('Immutable tuple: ', tuple_)
tuple_1 = 5, 10, ["Commet", True]
print(tuple_1)
tuple_1[2][1] = False
print(tuple_1)

list = [5, 10, 15, 12]
print(list)
print('Mutable list: ')
list[1] = 10
print(list)
list.append('Modified')
print(list)
list.extend('Language')
print(list)
list.remove(15)
print(list)




