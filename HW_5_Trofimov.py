import os
import json

print("""#1. Создаем файл программно, если файл есть - записываем в него данные построчно, выход из записи - пустая строка, в конце проверяем данные и удаляем файл""") # exercise 1

file_check = os.path.exists('text_1.txt') # проверка на наличие файла в директории

if file_check is True:
    my_file = open("text_1.txt", "w") # редактируем файл, если существует
else:
    my_file = open("text_1.txt", "x")  # создаем файл, если такого не существует

while True:
    content = my_file.write(input("Введите строку: ")) # создаем контент в файле
    my_file.write('\n') # добавляем новую строку в файле
    if not content: # если контента нет, останавливаем запись
        break

my_file.close() # закрываем файл

# блок проверки данных в файле:

open_my_file = open("text_1.txt") # open
print(open_my_file.read()) # read
open_my_file.close() # close
# os.remove("text_1.txt") # # можем удалить файл

print("#2. Считаем кол-во строк и в каждой строке кол-во символов в готовом файле") # exercise 2

count_lines = 0 # счетчик для кол-ва строк
count_lines_into = 0 # счетчик для кол-во строк, в подсчете символов

# почему пока в файле был русский текст мне выдавалась ошибка?
with open('text_2.txt', 'r') as f_obj: # считаем строки
    for item in f_obj:
        count_lines += 1

print('Всего строк в файле', count_lines) # считаем символы в строке

with open('text_2.txt', 'r') as f_obj:
    for item in f_obj.readlines():
        count_lines_into += 1
        print('В строке номер', count_lines_into, ', кол-во символов равно', len(item))

print("#3. Записываем фамилию и оклад сотрудника, считаем оклады сотрудников в готовом файле") # exercise 3

dict_salary = {} # из записей в файле сделаем словарь
with open('trofimov_salary.txt', 'r') as f_salary:
    for item in f_salary: # для каждой строки
        key, value = item.split() # строку переводим в список, элементы списка делаем ключом: значением
        dict_salary[key] = int(value) # определяем ключ-значение

print("Наш файл в виде словаря:", dict_salary)
print("ЗП меньше 20000: ", {k : v for k, v in dict_salary.items() if v < 20000})
print("Сумма ЗП всех сотурдников:", sum(dict_salary.values()))

print("#4. Открыть файл считать one, two, three, заменить и записать в новый файл") # exercise 4

digits_rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'} # словарь создали
new_file = []

# меняем англиское на русское
with open('digits.txt', 'r') as d_obj:
    for item in d_obj:
        item = item.split(' ', 1) # каждую строку сплитим 1 раз с сепаратором пробел т.е. на one и остальное
        new_file.append(digits_rus[item[0]] + '  ' + item[1]) # мемняем английское на русское + значение
    print(new_file)

# записываем в файл, если файл нет - создаем
with open('digits_rus.txt', 'w') as d_obj_rus:
    d_obj_rus.writelines(new_file)

# os.remove('digits_rus.txt') # # можем удалить файл

print("#5. Создать программно файл, записать числа через пробел и вывести сумму чисел")

def my_sum_list(numList): # функция суммирования списка
    sum_list = 0
    for item in numList:
        sum_list = sum_list + item
    return sum_list

file_chk_sum_num = os.path.exists('sum_numbers.txt') # проверка на наличие файла в директории

if file_chk_sum_num is True:
    with open("sum_numbers.txt", "w") as my_sum: # редактируем файл, если существует
        my_sum.write(input("Введите числа через пробел: "))

else:
    with open("sum_numbers.txt", "x") as my_sum: # создаем файл, если такого не существует
        my_sum.write(input("Введите числа через пробел: "))

open_ms = open("sum_numbers.txt", 'r') # открываем на чтение

digits_list = open_ms.read().split() # делаем список

numbers_list = [int(item) for item in digits_list] # список делаем числами

print("Сумма чисел в файле: ", my_sum_list(numbers_list)) # считаем сумму функцией

open_ms.close() # закрываем
# os.remove("sum_numbers.txt") # можем удалить файл

print("#6. Посчитать лекции, сделать словарь")

final_dict = {} # новый словарь
with open('lectures.txt', 'r') as init_f:
    for line in init_f:
        subjects = line.split() # делим строку на части
        sum_hours = sum([int(item) for item in subjects[1:]]) # считаем сумму часов
        final_dict[subjects[0]] = sum_hours # предмет - сумма часов
    print(f'Сумма часов по предмету - \n {final_dict}')

print('#7. Json. Прибыль, средняя прибль')

profit = {}
prof_dict = {}
prof = 0
prof_aver = 0
counter = 0
with open('firms.txt', 'r') as file:
    for line in file:
        name, firm, earning, cost = line.split()
        profit[name] = int(earning) - int(cost)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            counter += 1
    if counter != 0:
        prof_aver = prof / counter
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    prof_dict = {'средняя прибыль': round(prof_aver)}
    profit.update(prof_dict)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')