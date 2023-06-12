from copy import copy, deepcopy

# immutable

# int
num_1 = 10
print(id(num_1))
num_2 = num_1
print(id(num_2))
num_2 = 11
print(id(num_2))
print(num_1)
print(num_2, '\n')

# str
str_1 = 'string'
print(id(str_1))
str_2 = str_1
print(id(str_2))
str_2 = 'string_2'
print(id(str_2))
print(str_1)
print(str_2, '\n')

# tuple
a = (1, 2, 3, 4)
print(id(a))
b = a
print(id(b))
b = ('a', 'b')
print(id(b))
print(a)
print(b, '\n')

# mutable

# list
lis = [1, 2, 3]
print(id(lis))
lis_2 = lis
print(id(lis_2))
lis_2.append(4)
print(id(lis_2))
print(lis)
print(lis_2, '\n')

# solution
old_list = ['a', 'b', 'c', 'd']
print(id(old_list))
new_list = old_list[:]
print(id(new_list))
new_list.append('e')
print(old_list)
print(new_list, '\n')

# copy and deepcopy

# Разница между неглубоким и глубоким копированием актуальна
# только для составных объектов -- коллекций
# (объектов, содержащих другие объекты, такие как списки, словари,
#  кортежи или экземпляры классов):


# copy
# Неглубокая копия создает новый составной объект, а затем
# (насколько это возможно)
# вставляет в него ссылки на объекты, найденные в оригинале.

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

clone = copy(c)
print(id(c))
print(id(clone))
print(c)
clone[0][2] = 5
print(clone)
print(c, '\n')


# deepcopy
# Глубокая копия создает новый составной объект,
# а затем рекурсивно вставляет в него копии объектов, найденных в оригинале.
# Deepcopy в отличие от простого copy копирует ссылки вложенных объектов тоже

deep = deepcopy(c)
print(deep)
deep[0][1] = 10
print(deep)
print(c, '\n')
