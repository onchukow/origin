# Задание 1. Создать список, вывести типы элементов списка
list_1 = [16, 9.0, 'some text', ['element_1', 2], None, {"age": 23, "sex": "male"}, ("tuple_item", 5.0)]
for element in list_1:
    print(type(element))

# Задание 2. Реализовать обмен значений списка. При нечетном количестве последний элемент оставить на своем месте
change = []
k = 0
while len(change) < 5:
    addition = input('Print an element for the list: ')
    if addition == 'stop':
        break
    else:
        change.append(addition)

for part in range(len(change)):
    if k < len(change):
        k = part + 1
        if k % 2 == 1:
            try:
                change[part], change[k] = change[k], change[part]
            except IndexError:
                break
        else:
            continue
    else:
        break

print('List with changed numbers: ', change)

# Задание 3. При помощи словарей и списков в ответ на номер месяца сообщить время года
seasonlist = ['Winter', 'Spring', 'Summer', 'Autumn']
seasondic = {'Winter': [1, 2, 12], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
month = 0
while (month < 1 or month > 12) or type(month) != int:
    month = input('Enter a number of month: ')
    try:
        month = int(month)
    except ValueError or TypeError:
        month = 0
        continue

if month > 2 and month < 6:
    print(seasonlist[1])
elif month > 5 and month < 9:
    print(seasonlist[2])
elif month > 8 and month < 12:
    print(seasonlist[3])
else:
    print(seasonlist[0])

for items in seasondic:
    if month in seasondic.get(items):
        print(items)
        break
    else:
        continue

# Задание 4. Ввод слов через пробел. Вывод: нумерованный список с новой строки + длина слова не больше 10
line = input('Please enter some words with spaces: ')
linelist = line.split(' ')
for counter, item in enumerate(linelist, 1):
    print(counter, item[:10])

# Задание 5. Есть список целых чисел, расставленный по убыванию. Пользователь вводит число, которое должно добавится к
# списку в нужном месте. В начале, если больше других, рядом с такими же и в конце, если меньше всех

results = [7, 5, 3, 3, 2]
results = sorted(results, reverse=True)
user = float(input('Please enter a new result (for check position !float! number used): '))
coin = len(results) + 1
for count in results[::-1]:
    coin -= 1
    if count >= user:
        results.insert(coin, user)
        break
    elif count == results[0]:
        results.insert(0, user)
        break

    else:
        continue

print('New result entered to the list: ', results)

# Задание 6*. Нужно поиграть со списками. Ограничение на количество элементов товара ограничено 3, но можно исправить
# в цикле. При этом стоит ограничение на 5 вводов на всякий случай с прерыванием.
goods = []
name = []
price = []
amount = []
unit = []
goods_inf = {'Name': name, 'Price': price, 'Amount': amount, 'Unit type': unit}
data = 0
i = 0
item_dic = {}
value_list = []

while data != 'stop' and data != 'exit' and data != 'quit' and len(name) < 3:
    name.append(input('Please input a name of good: '))
    price.append(float(input('Please input a price of good: ')))
    amount.append(int(input('Please input an amount of goods: ')))
    unit.append(input('Please input a unit type: '))
    goods_inf.update({'Name': name, 'Price': price, 'Amount': amount, 'Unit type': unit})

    for good in goods_inf:
        list_one = goods_inf.get(good)
        op_dic = dict.fromkeys([good], list_one[i])
        item_dic.update(op_dic)

    i += 1
    all_data = item_dic.copy()
    lst = tuple([i, all_data])
    value_list.append(lst)
    data = input('Add one more good? !!! For exit "stop" !!! Enter to continue ')

    if i == 5:
        break

print('Values structure: ', value_list)
print('Analytic dictionary: ', goods_inf)
