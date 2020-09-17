print("#1")

my_text = "мой_текст"
my_int = 7
my_float = 10.5
my_bool = True

print(my_text)

print(my_int)

print(my_bool)

user_txt = str(input("Введите текст: "))
user_int = int(input("Введите целое число: "))
user_bool = bool(input("Введите Да или Нет: "))

print(user_txt)

print(user_int)

print(user_bool)


print("#2")

ct = int(input("Введите время в секундах: "))

ch = int(ct) // 3600
cm = (int(ct) // 60) % 60
cs = int(ct) % 60

if ch < 10:
    ch = '0'+str(ch)
else:
    ch
if cm < 10:
    cm = '0'+str(cm)
else:
    cm
if  cs < 10:
    cs = '0'+str(cs)

print(ch, ":", cm, ":", cs)

print("#3")

int_d = int(input("Введите целое число: "))

nn = str(int_d) + str(int_d)
nnn = str(int_d) + str(int_d) + str(int_d)

result = int(int_d) + int(nn) + int(nnn)

print(result)

print("#4")

n = int(input("Введите целое не отрицательное число: "))
m = n % 10
n = n // 10

while n < 0: #ноль целое не отрицательное число, его можно вводить
    n = int(input("Я повторяю, введите целое не отрицательное число: "))
else:
    while n > 0:
        if n % 10 > m:
            m = n % 10
        n = n // 10

print(m)

print("#5")

rev = float(input("Выручка: "))
cost = float(input("Затраты: "))

if rev > cost:
    profit = rev - cost
    ren = profit / rev
    print("Есть прибыль, рентабельность составила: ", ren)
    emp = int(input("Сколько у вас сотрудников? "))
    pou = profit / emp
    print("Прибыль на 1 сотрудника составила - ", pou)
else:
    print("Нет прибыли")


print("#6")

a = float(input("Введите дистанцию спортсмена в первый день: "))
b = float(input("Какую дистанцию в день хочет пробегать спортсмен?:  "))
num = 1

print("В ", num, " день спортсмен пробежал: ", a)

while a < b:
    a = a + (a * 0.1)
    num = num + 1
    print("В ", num, " день спортсмен пробежал: ", a)

print(num, " дней потребуется спортсмену, чтобы бегать больше ", b, " км в день!")