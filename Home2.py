# В первой строке файла находится информация об ассортименте мороженного, 
# во второй - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»

file = open('ice.txt', encoding='utf-8')

ice = file.readlines(1)
empty = file.readlines(2)
file.close()

list1 = ice[0].split(', ')
list2 = empty[0].split(', ')
a = set(list1)
b = set(list2)
print(a.difference(b))