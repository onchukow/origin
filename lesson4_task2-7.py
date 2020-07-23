from itertools import count, cycle
from random import randint
from functools import reduce
from math import factorial

# Задание 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых
# больше предыдущего элемента.

generator_list = [randint(0, 300) for i in range(10)]
print('Randomly generated list: ', generator_list)
list_new = [num for num in generator_list[1:] if num > generator_list[generator_list.index(num) - 1]]
print('List with removed counts > previous, except [0]: ', list_new)

# Задание 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

print([count for count in range(20, 241) if count % 20 == 0 or count % 21 == 0])

# Задание 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования
# в исходном списке. Для выполнения задания обязательно использовать генератор.

task4_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([amm for amm in task4_list if task4_list.count(amm) == 1])

# Задание 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
# произведения всех элементов списка.

task5_list = [obj for obj in range(100, 1001) if obj % 2 == 0]


def multi(x, y):
    return x * y


print(reduce(multi, task5_list))

# Задание 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

for tt in count(3, ):
    if tt > 10:
        break
    print(tt)

task6_list = [randint(0, 50) for i in range(3)]
print(task6_list)
list_empty = []
x = 0
for el in cycle(task6_list):
    if x > 11:
        break
    list_empty.append(el)
    x += 1
print(list_empty)

# Задание 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24


n = int(input('Input n for factorial: '))
numb = 1


def fact(x):
    for ele in range(1, x + 1):
        yield factorial(ele)


for el in fact(n):
    print(numb, '! = ', el)
    numb += 1
