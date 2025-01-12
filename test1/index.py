print('''
      Привет! Это калькулятор процентов!
      Ниже введи "Дано" свое задачи, где будет a/b/c
      ''')
print('Введи A')
a = int(input())
print('Введи B')
b = int(input())
print('Введи C')
c = int(input())
n = a + b + c 
print('Введи кол-во участников о которых тебе следует узнать.')
t = int(input()) 
x = t / n * 100 
print('Ответ%:')
print(x)