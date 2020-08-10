# Task 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    data = input('Enter the data: ')

    @classmethod
    def data_sep(cls):
        line = [int(i) for i in cls.data.split('-')]
        return line

    @staticmethod
    def data_check(data):
        checkline = [int(i) for i in data.split('-')]
        if checkline[0] < 1 or checkline[0] > 31:
            return ValueError, 'Day is not acceptable'
        if checkline[1] < 1 or checkline[1] > 12:
            return ValueError, 'Month is not acceptable'
        if checkline[2] < 0:
            return 'Years before BC are not acceptable'
        else:
            return data, 'is acceptable'


a = Data()
print(a.data_sep())
print(Data.data_check('15-12-2020'))


# Task 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на
# данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class ZeroError(Exception):
    def __init__(self, data):
        self.data = data


inp_data = input("Enter two numbers for division x/y with space: ")
inp_data = inp_data.split(' ')
try:
    x = float(inp_data[0])
    y = float(inp_data[1])
    if y == 0:
        raise ZeroError("Division on 0 is impossible!")
except ValueError:
    print("Only numbers are acceptable!")
except ZeroError as err:
    print(err)
else:
    print(f"Your result: {x / y}")


# Task 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.

class Digits(Exception):
    def __init__(self, inps):
        self.inps = inps


checklist = []
inputes = ''
while True:
    inputes = input('Enter a values: ')
    if inputes == 'stop' or inputes == 'quit':
        break
    try:
        if inputes.isdigit() == 0:
            raise Digits('Only numbers are acceptable')
    except Digits as err:
        print(err)
    else:
        checklist.append(inputes)

print(checklist)


# Task 5-6 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Store:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price is: {self.price} quantity: {self.quantity}'

    def reception(self):

        try:
            unit = input(f'Enter a name: ')
            unit_p = int(input(f'Price per one: '))
            unit_q = int(input(f'Quantity: '))
            unique = {'Model': unit, 'Price': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'List: -\n {self.my_store}')
        except:
            return f'Data error occurred'

        print(f'For quit - Q, to continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Store: \n {self.my_store_full}')
            return f'Exit'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Store):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Store):
    def to_copier(self):
        return f'to copier smth {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())


# Task 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Sum result: ')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Multiple result: ')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(2, -1)
z_2 = ComplexNumber(50, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
