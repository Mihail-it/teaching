txt1 = list('123')
txt2 = list('456')

txt1.extend(txt2)
# .extend - Объединение списков
print(txt1)

txt3 = list('123')
txt4 = list('456')
print(txt3 + txt4)
# Объединение списков с помошью "+"

lst21 = [1, 2, 3, 1, 4]
print(lst21.index(1, 2, 4))
# .index Поиск индекса элемента по его значению

ls123t = [1, 2, 3]
res = 1 in ls123t
print(res)
# Проверка наличия элемента в списке

lst6 = [1, 2, 1, 3]
print(lst6.count(1))
# .count - найти количество совпадений элемента в списке

lst111 = [1, 2, 3]
lst111.reverse()
print(lst111)
# .reverse - перевернуть все элементы в списке в обратном порядке


lst222 = [3, 2, 1]
lst222.sort()
print(lst222) 
# .sort Сортировка элементов '123abc'

lst333 = [3, 2, 1]
res = sorted(lst333)
print(res)
# sorted Сортировка элементов в копии списка

lst = ['1', '2', '3']
res = '-'.join(lst)
print(res)
#  res = 'символ' .join(name) - слияние списка через символ указан в ''


