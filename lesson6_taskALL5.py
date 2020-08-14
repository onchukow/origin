import time


# Task 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

def timer(x):
    change = time.time() + x
    while time.time() < change:
        pass


class Trafficlight:
    __color = ['RED', 'YELLOW', 'GREEN']

    def __init__(self):
        count = 0
        while count < 2:
            count += 1
            print(Trafficlight.__color[0])
            timer(7)
            print(Trafficlight.__color[1])
            timer(2)
            print(Trafficlight.__color[2])
            timer(5)
            print(Trafficlight.__color[1])
            timer(2)


a = Trafficlight()


# Task 2 Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        _weight = 25
        _height = 5
        print(_length * _width * _weight * _height / 1000, 'tons is needed')


road_example = Road(20, 5000)


# Task 3 Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        total = int(self._income.get('wage')) + int(self._income.get('bonus'))
        print('Total income is: ', total)


petrov = Position('Vasiliy', 'Petrov', 'Lawyer', 5000, 1000)
petrov.get_total_income()
petrov.get_full_name()
print(petrov.name)


# Task 4 Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = is_police

    def go(self):
        print('Car is driving')

    def turn(self, direction):
        self.direction = direction
        print('Car turned', direction)

    def stop(self):
        print('Car stopped')

    def show_speed(self):
        print('Current speed is', self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
        self.police = is_police
        self.police = False

    def show_speed(self):
        if self.speed > 60:
            print('WARNING')
        super(TownCar, self).show_speed()


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
        self.police = is_police
        self.police = False

    def show_speed(self):
        if self.speed > 40:
            print('WARNING')
        super(WorkCar, self).show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
        self.police = is_police
        self.police = True


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
        self.police = is_police
        self.police = False


new_car = TownCar(100, 'white', 'Opel', 1)
new_car.show_speed()
print(new_car.police)

wiu_wiu = PoliceCar(100, 'blue', 'Ford', 0)
wiu_wiu.show_speed()
print(wiu_wiu.police)
wiu_wiu.go()
wiu_wiu.stop()
wiu_wiu.turn('left')


# Task 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Drawing initialisation...')


class Pen(Stationery):
    def draw(self):
        print('Pen is penning!')


class Pencil(Stationery):
    def draw(self):
        print('Pencil is penciling!')


class Handle(Stationery):
    def draw(self):
        print('Handle is handling!')


a = Pen('Krause')
a.draw()
b = Pencil('Erich')
b.draw()
f = Handle('Bork')
f.draw()
e = Stationery('Lorka')
e.draw()
