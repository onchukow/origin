print('Welcome to simple based calculator! \n'
      'List of included operations: \n '
      '1. Sum (sum) \n '
      '2. Submission (sub) \n '
      '3. Multiply (mult) \n '
      '4. Divide (div) \n '
      '5. Exponential (exp) \n'
      
      '\n Print "exit" to stop this program\n ' )
func = 0

while func != 'exit':
    x = input('Please input a number x: ')
    if x == 'exit':
        break
    y = input('Please input a number y: ')
    if y == 'exit':
        break
    x = int(x)
    y = int(y)
    res = 0
    func = input('Please choose an operation sum/sub/mult/div/exp: ')
    if func == 'sum':
        res = x + y
        print("Operation's result is: ", res)
    elif func == 'sub':
        res = x - y
        print("Operation's result is: ", res)
    elif func == 'mult':
        res = x * y
        print("Operation's result is: ", res)
    elif func == 'div':
        res = x / y
        print("Operation's result is: ", res)
    elif func == 'exp':
        res = x ** y
        print("Operation's result is: ", res)
    elif func == 'exit':
        print("Goodbye!")
    else:
        print('You have chosen not described operation')

