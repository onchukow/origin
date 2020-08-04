import io
import json

# Task 1 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("task_1.txt", 'a') as task_1:
    a = 0
    while a != '':
        a = input('Please enter some data: ')
        print(a, file=task_1)

# Task 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

task_2 = open('task_2.txt', 'r')
num = 0
for counter, line in enumerate(task_2, 1):
    words = line.split(' ')
    a = len(words)
    print(f'Line {counter} contains {a} words')
    words.clear()
    num += 1
print('Total lines: ', num)
task_2.close()


# Task 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.

class Salaries:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name


task_3 = open('task_3.txt', 'r')
lines_count = 0
whole_salaries = 0
for line in task_3:
    lines_count += 1
    a = line.split(' ')
    line = Salaries(a[0], a[1])
    whole_salaries += int(line.salary)
    if int(line.salary) < 20000:
        print(f'{line.name} has salary less than 20000 RUB')
average = whole_salaries // lines_count
print(f'Average salary of {lines_count} employees is {average} RUB')

task_3.close()

# Task 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.

count_dic = {'One': 'Eins', 'Two': 'Zwei', 'Three': 'Drei', 'Four': 'Vier'}
task_4 = open('task_4.txt', 'r')
file_name = 1.0
for line in task_4:
    if line == '' or line == '\n':
        file_name += 1
        continue
    else:
        task_4_0 = open(f'{file_name}.txt', 'a')
        a = line.split(' - ')
        a[0] = count_dic.get(a[0])
        task_4_0.write(f'{a[0]} - {a[1]}')
        task_4_0.close()
task_4.close()

# Task 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

task_5 = open('task_5.txt', 'a')
some_numbers = input('Please input some numbers separated with spaces: ')
task_5.write(' ' + some_numbers + ' ')
sum_num = 0
task_5 = open('task_5.txt', 'r')
for line in task_5:
    numbers_list = line.split(' ')
    for num in numbers_list:
        try:
            sum_num += int(num)
        except:
            continue
print('Sum of all numbers is: ', sum_num)
task_5.close()

# Task 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести словарь на экран.

dict_task = {}

task_6 = open('task_6.txt', 'r')
for line in task_6:
    name, nums, numslst, calc = '', '', [], 0
    for letter in line:
        if letter != ':':
            name += letter
        else:
            break
    for letter in line:
        if letter.isdigit():
            nums = nums + letter
        elif nums != '':
            numslst.append(int(nums))
            nums = ''
    for num in numslst:
        calc += num
    dict_task[name] = calc

print(dict_task)
task_6.close()

# Task 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

task_7 = open('task_7.txt', 'r')
task7_dict, aver, count, average = {}, {}, 0, 0

for line in task_7:
    firms_lst = (line.split(' '))
    profits = int(firms_lst[2]) - int(firms_lst[3])
    task7_dict[firms_lst[0]] = profits
    average += int(firms_lst[2])
    count += 1
aver['average_profit'] = average // count
task_7_lst = [task7_dict, aver]
print(task_7_lst)
task_7.close()
with open('task_7.json', 'w') as json_7:
    json.dump(task_7_lst, json_7)
