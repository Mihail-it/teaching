print('''
      Привет! Это калькулятор процентов!
      Ниже введи "Дано" свое задачи, где будет a/b/c
      ''')
a = int(input('Введи A: '))
b = int(input('Введи B: '))
c = int(input('Введи C: '))
n = a + b + c 
t = int(input('Введи кол-во участников о которых тебе следует узнать: ')) 
x = t / n * 100 
print('Ответ%:')
print(x)

print('Book https://code.mu/ru/python/book/prime/')