print("#1") #exercise 1

my_list_for_type = ["Мясо", 1, True, 1.5]

for check_type in my_list_for_type: #создаем переменную check_type для проверки типов элементов в списке
    print(type(check_type)) #возвращаем тип элемента через функцию type

print("#2") #exercise 2

user_str = input("Введите любые символы: ")
user_str_reverse = ''
user_list = list(user_str)

try:
    # разбиваем список на элементы
    for num_el in range(len(user_list)):
        if num_el % 2 == 0: #если элементы четный, то
            tmp = user_list[num_el] #записываем номер элемента в переменную tmp
            user_list[num_el] = user_list[num_el + 1] #присваиваем значение следующего элемента
            user_list[num_el + 1] = tmp #передаем полученное значение в на нужный элемент
except IndexError:
    # для последнего эл-нта не будет следующего индекса элемента, поэтому оставляем поседний эл-нт
    tmp = user_list[-1]

user_str_reverse = ''.join(user_list) #ответ на задачу

#для сравнения выведем пользовательское значение и ответ по задаче:
print(user_str)
print(user_str_reverse)

print("#3.1 решение через list") #exercise 3.1

user_month = int(input("Введите месяц от 1 до 12: "))

#убираем возможность введения некорректного месяца
while user_month < 1 or user_month > 12:
    user_month = int(input("Введите месяц я сказал: "))

#нумеруем список начиная с номера 1
for ind, season in enumerate(['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима'], 1):
        if user_month == ind: #ищем в списке введенный месяц
            user_season = season #присваиваем переменной значение нужного элемента

print("Месяц №", user_month, "- это", user_season)

print("#3.2 решение через dict") #exercise 3.2

user_month1 = int(input("Введите месяц от 1 до 12: "))
#содаем словарь сезонов
dict_season = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето', 7:'лето', 8:'лето', 9:'осень', 10:'осень', 11:'осень', 12:'зима'}

#убираем возможность введения некорректного месяца
while user_month1 < 1 or user_month1 > 12:
    user_month1 = int(input("Введите месяц я сказал: "))

user_season1 = dict_season.setdefault(user_month1) #присваиваем переменной значение нужного элемента из словаря

print("Месяц №", user_month1, "- это", user_season1)


print("#4") #exercise 4

user_text = input("Введите несколько слов через пробел: ").split() #создаем список слов

for num, text in enumerate(user_text, 1): #нумеруем список
    print(num, text[0:9]) #отрезаем лишнее

print("#5") #exercise 5

my_rate = [100, 9, 8, 7, 5, 2, 1] # изначальный рейтинг
user_rate = int(input("Введите элемент рейтинга (натуральное число): ")) # новый элемент рейтинга

my_rate.append(user_rate) # добавляем новый элемент в рейтинг
my_rate.sort() # сортируем по возрастанию
my_rate.reverse() # разворачиваем сортировку по убыванию

print("Пользователь ввел число", user_rate, ".", "Результат:", my_rate)


