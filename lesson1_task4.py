main = input('Please enter a number: ')
i = len(main)
try:
    main = int(main)
    calc = []
    a = 0
    while i != 1:
        a = (main // 10 ** (i-1)) % 10
        calc.append(a)
        i -= 1
    b = main % 10
    calc.append(b)
    print(max(calc))
except ValueError:
    print('Number should be entered')


