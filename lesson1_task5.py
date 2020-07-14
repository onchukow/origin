debit = input("Please input your company's earnings for the previous year (USD): ")
credit = input("Please input your company's expenses for the previous year (USD): ")
try:
    debit = int(debit)
    credit = int(credit)
    calc = 0
    if (debit - credit) > 0:
        print('Your company indicated a profit last year')
        calc = round((((debit - credit) / credit) * 100), 2)
        #Я пытался сделать различные варианты расчета рентабельности, но этот мне показался самым нормальным
        print(f'Your ROE for the previous year: {calc:2}%')
        emp = int(input('Please input amount of employees: '))
        calcemp = round(((debit - credit) / emp), 2)
        print(f"Every employee gains around {calcemp} USD for the company")
    elif (debit - credit) == 0:
        print('You have awesome accountants!')
    else:
        print('Your company indicated losses last year')
except ValueError:
    print('Only numbers applicable')


