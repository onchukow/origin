# Задание 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide_task(x, y):
    try:
        z = x / y
        print('Your result is: ', z)
    except ZeroDivisionError:
        print('Division on zero is impossible')


number_1 = float(input('Enter number 1: '))
number_2 = float(input('Enter number 2: '))

divide_task(number_1, number_2)

# Задание 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

name_inp = input('Enter your name: ')
surname_inp = input('Enter your surname: ')
year_inp = input('Enter you date of birth dd/mm/yyyy: ')
city_inp = input('Enter your city of residence: ')
email_inp = input('Enter your e-mail: ')
phone_inp = input('Enter your phone: ')


def data_collect(**kwargs):
    a = ''
    for i in kwargs.values():
        a += i + ' '
    print(a)


data_collect(name=name_inp, surname=surname_inp, year=year_inp, city=city_inp, email=email_inp, phone=phone_inp)


# Задание 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    my_func_list = [x, y, z]
    my_func_list.remove(min(my_func_list))
    a = sum(my_func_list)
    print('Sum of the biggest values is: ', a)


my_func(x=4, y=1, z=5)


# Задание 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def pow_func(x, y):
    powpow = 1
    try:
        if y > 0:
            for i in range(1, (y + 1)):
                powpow *= x
            print('Result: ', powpow)
        elif y < 0:
            for i in range(1, (y * (-1) + 1)):
                powpow *= x
            print('Result: ', 1 / powpow)
        elif y == 0:
            print('Result: ', powpow)
    except Exception:
        print('Error with vars occured')


pow_func(-2, -3)


# Задание 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
# выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def summable():
    a = 0
    ch = 1
    while True:
        whole_str = input('Please input a string with interegable separated with spaces: ')
        whole_list = whole_str.split(' ')
        for i in whole_list:
            try:
                i = int(i)
                a += i
            except ValueError:
                ch = False
                break
        print('Result: ', a)
        if ch == False:
            break
        else:
            continue


summable()


# Задание 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу
# должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать
# написанную ранее функцию int_func().

def int_func(x):
    return x.title()


print(int_func(input('Enter a string: ')))
