from itertools import cycle, count
from functools import reduce

print("#1") #exercise 1

print('''Для проверки первого задания необходимо запустить из консоли скрипт trofimov_salary.py с тремя параметрами:
где параметр 1 - это часы, 2 - это ставка, 3 - это премия
пример выполнения в косоли: python c:trofimov_salary.py 168 1000 20000''')

print("#2") #exercise 2

# пзапрашиваем у пользователя ряд чисел, преобразуем в int каждый итем
new_list = [int(item) for item in input("Enter several numbers with SPACE separator: ").split()]

# сраваниваем каждое следующее значение с преыдущим
result_list = [new_list[i] for i in range(1, len(new_list)) if new_list[i] > new_list[i - 1]]

print(result_list)

print("#3") #exercise 3

# кратные 20 и 21 числа
print([i for i in range(20, 240) if (i % 20 == 0 or i % 21 == 0)])

print("#5") #exercise 5

# произведение четных чисел в рэндже 100-1000 (указал 1001, чтобы включить 1000)
print(reduce(lambda one, two: one * two, [i for i in range(100, 1001) if i % 2 == 0]))

print("#6") #exercise 6

uniq_list = [2, 3, 5, 10, 15, 2, 7, 6] # какие-то рандомные значения в списке

# счетчик с выходом после 10
for item in count(3):
    if item > 10:
        break
    else:
        print(item)

counter = 0

# цикл принта с выходом после 10 повторений, цикл бежит по списку uniq_list
for item in cycle(uniq_list):
    if counter > 10:
        break
    print(item)
    counter = counter + 1

print("#7") #exercise 7

# функция факториала

def my_fact(n):
    if n == 0:
        return 1
    yield my_fact(n - 1) * n

# далее я завис

