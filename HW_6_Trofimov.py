from time import sleep

print('#1. TrafficLight и его цвета')

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый'] # возможные цвета

    def running(self):
        i = 0 # итератор
        while i <= 2:
            print(f'{TrafficLight.__color[i]}') # показываем цвет
            if i == 0:
                sleep(7) # ожидание в секундах
            if i == 1:
                sleep(5)
            if i == 2:
                sleep(7)
            i = i + 1 # выход из цикла, иначе зависнем на красном

new_tl = TrafficLight() # создаем экземпляр класса
new_tl.running() # вызываем метод running

print('#2. Road и масса асфальта')

class Road:

    def __init__(self, _length, _width): # _защищенные переменные
        self._length = _length
        self._width = _width

    def weight(self): # метод расчета площади
        return self._length * self._width

    def total(self, volume): # метод расчета общей массы
        return self.weight() * volume

mass = Road(5, 5)
print(mass.total(10))

print('#3. Worker и Position')

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position

       # if type(wage) and type(bonus) is int:
       #      self._income = {'оклад': int(wage), 'премия': int(bonus)}
       #  else:
       #      self.wage = int(input('Вы ввели не число, введите оклад повторно: '))
       #      self.bonus = int(input('Вы ввели не число, введите премию повторно: '))

        self._income = {'оклад': int(wage), 'премия': int(bonus)}  # делаем словарь из переменных wage и bonus

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus) # обращаемся к классу-родителю

    def get_full_name(self):
        return self.name + ' ' + self.surname # конкатинируем string

    def get_total_income(self):
        return self._income.get('оклад') + self._income.get('премия') #суммируем int

my_pos = Position('Артем', 'Трофимов', 'Аналитик', 130000, 40000)
print(my_pos.get_full_name())
print(my_pos.position)
print(my_pos.get_total_income())

print('#4.Cars')

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая сокрость {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышена'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):

        if self.is_police is True:
            return f'{self.name} - это полиция'
        else:
            return f'{self.name} - это не полиция'

kia = TownCar(70, 'Серый', 'Kia', False)
bmw = SportCar(300, 'Золотой', 'BMW', False)
zil = WorkCar(50, 'Зеленый', 'ZIL', False)
vw = PoliceCar(100, 'Белый',  'VW', True)

print(
f'Когда {kia.turn_right()} по главной дороге, а по второстепенной {bmw.go()} - случилась авария, тут {vw.stop()} ({vw.police()})\n'
f'и выписала для {bmw.name} штраф, но правда теперь водителю {kia.name} придется перекрашивать {kia.color} в {vw.color} \n'
f'А {zil.name} сами знаете, что возил. Вот такая вот ситуация.'
)

print('#5. Канцелярская принадлежность')

class Stationary: # базовый класс

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self.title} | Запуск отрисовки {self.title.replace(self.title, "говной")}'


class Pen(Stationary): # дочерний класс с обращением к базовому и в методе draw возвращаем название title и текст
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} | Запуск отрисовки ручкой'


class Pencil(Stationary): # дочерний класс с обращением к базовому и в методе draw возвращаем название title и текст
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} | Запуск отрисовки карандашом'


class Handle(Stationary): # дочерний класс с обращением к базовому и в методе draw возвращаем название title и текст
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} | Запуск отрисовки маркером'


crap = Stationary('Розовая акварель')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

print(crap.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())