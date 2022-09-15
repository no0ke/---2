

# Работа с файлом:
# Переменные и файл, модификаторы работы:
# a-открытие для добавления данных
# r-открытие для чтения данных
# w- открытие для записи данных
# w+ и r+
# Код для работы с файлами:
#  with open('file.txt', 'w') as data: # Перый способ
#  data.write('line 1\n')
#  data.write('line 2\n')

# colors = ['red', 'green', 'blue'] # Второй способ
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data: 
#  print(line)
# data.close()
2
# Функции
# Это фрагмент программы, используемый 
# многократно
# def function_name(x):
# # body line 1
# # . . .
# # body line n
#  # optional return
3
# import function_file as ff  - Импорт функции и присваивание псевданима для сокращения
4
# Рекурсия - Вызов функции самой себя.
# Пример:
# def fib(n):
#  if n in [1, 2]:
#  return 1
#  else:
#  return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34
