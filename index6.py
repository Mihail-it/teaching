# lesson 100
dct = {
	'a': 1,
	'b': 2,
	'c': 3
}
res = list(dct)
print(res)
# Преобразование словоря в список

res = dct.keys()
print(res)
# Выведет все ключи из словоря

res = dct.values()
print(res)
# Выведет все значения из словоря

dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct2 = {
	1: 'a',
	2: 'b',
	3: 'c'
}
res1 = list(dct1.values())
res2 = list(dct2.values())
abc = res1 + res2
print(abc)

dct = {
	'a': 1,
	'b': 2,
	'c': 3
}
item = tuple(dct.items())
print(item)
# Выведет пары, ключ - значение

dct123 = {
	'1': 12,
	'2': 24,
	'3': 36
}

dct221 = {
	'a': '3',
	'b': '6',
	'c': '9'
}
sty111 = dct123['1']
sty222 = dct123['2']
sty333 = dct123['3']
b  = int(sty111 + sty222 + sty333)

abc1 = int(dct221['a'])
abc2 = int(dct221['b'])
abc3 = int(dct221['c'])
a = int(abc1 + abc2 + abc3)
ab = b - a
print(ab)

i = 0 
while i < 10: # ключевое слово 'while' и условие выполнение цикла
    print(i) # вывод значения переменной i
    i += 1 # увеличение значения переменной i на единицу

