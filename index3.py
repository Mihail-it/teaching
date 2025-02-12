lst = ['4', '3', '2', '1']
res = '-'.join(lst)
print(res)
#  res = 'символ' .join(name) - слияние списка через символ указан в ''

tpl = ('a', 'b', 'c')
#  кортеж(не изменяемы)

tpl1 = ('1', '2', '3')
tpl2 = (1, 2, 3)
tpl3 = (True, False)
tpl4 = (['a', 'b'], ['c', 'd'])
# кортетж хранит строки, числа, булевые значения, списки

abc = tuple('123abc')
print(abc)
# tuple - создание кортежа

txt = '12345'
tpl1 = tuple(txt)
print(tpl1)
print(tpl1[1])
# выведет символ по индексу

tpl = ('a', 'b', 'c')
print(len(tpl))
# len - найти длину кортежа

tpl1 = ('a', 'b', 'c')
tpl2 = ('d', 'e')

res = tpl1 + tpl2
print(res)
# Объединение кортежа

tpl = ('a', 'b')
res = tpl * 2

print(res)
# Умножение кортежа

tpl = ('a', 'b' 'c')
res = 'a' in tpl

print(res)
# Проверка на наличе элемнта в кортеже
 
tpl = (2, 4, 6, 10)
res =  '8' in tpl
print(res)

tpl = ('abc', 'def')
res = 'd' in tpl
print(res)

tpl = ('a', 'b', 'c')
sosiska, sordelka, banan = tpl
# задали переменные для кортежа
print(sosiska, sordelka, banan)
# распаковка кортежей 

bro = (input('Введи да'))
ccc = tuple(bro)
ccc1 = list(ccc)
# сделали список из кортежа
print(ccc1)
print(ccc)

