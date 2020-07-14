main = input('Please enter a number: ')
calc_2 = main + main
calc_3 = calc_2 + main
try:
    result = int(main) + int(calc_3) + int(calc_2)
    print(result)
except ValueError:
    result = (main + calc_2 + calc_3)
    print(result)

