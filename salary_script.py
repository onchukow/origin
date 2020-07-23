# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

script_name, hours, wage, bonus = argv
salary = float(hours) * float(wage) + float(bonus)
print("Script's name: ", script_name)
print("Worker's salary is: ", salary, 'USD')
