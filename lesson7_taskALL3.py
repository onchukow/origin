# Task 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        b = ''
        nums = 0
        for line in self.lists:
            while len(line) < len(self.lists[nums - 1]):
                line.append(0)
            b += str(line) + '\n'
            nums += 1
        return b

    def __add__(self, other):
        sum = []
        brak = []
        output = ''
        for liss in self.lists:
            n = self.lists.index(liss)
            for ll in range(len(liss)):
                sum.append(((self.lists[n])[ll] + (other.lists[n])[ll]))
            brak.append(sum.copy())
            sum.clear()
        for part in brak:
            output += str(part) + '\n'
        return output


sample = Matrix([[1, 4, 3], [2, 1, 5], [3, 1, 2]])
sample2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(sample)
print(sample2)
print(sample + sample2)

# # Task 2 Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size, name):
        self.size = size
        self.name = name

    @abstractmethod
    def sizecount(self):
        pass


class Coat(Clothes):

    @property
    def sizecount(self):
        howmuch = round((self.size / 6.5 + 0.5), 1)
        return f'You need {howmuch} metres of material for {self.name} coat'


class Suit(Clothes):

    @property
    def sizecount(self):
        howmuch = self.size * 2 + 0.3
        return f'You need {howmuch} metres of material for {self.name} suit'


hugo = Coat(50, 'HUGO')
print(hugo.sizecount)
brioni = Suit(30, 'Brioni')
print(brioni.sizecount)


# Task 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
# клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n*****.

from math import floor

class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return f'Sum of cells = {self.count + other.count}'

    def __sub__(self, other):
        substract = self.count - other.count
        if substract <= 0:
            return 'Mission impossible :( Try to increase first cell'
        else:
            return f"Cells' substraction = {substract}"

    def __mul__(self, other):
        return f"Cells multiplied! New cell has a size of {self.count * other.count} shells"

    def __truediv__(self, other):
        return f"Cells divided. New cell has a size of {floor(self.count / other.count)} shells"

    def make_order(self, lines):
        string = '\n'.join(['*' * lines for nums in range(self.count // lines)]) + '\n' + '*' * (self.count % lines)
        return string


cell_a = Cell(15)
cell_b = Cell(4)

print(cell_a + cell_b)
print(cell_a - cell_b)
print(cell_b - cell_a)
print(cell_a * cell_b)
print(cell_a / cell_b)
print(cell_a.make_order(6))
