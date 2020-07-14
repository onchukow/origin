time = int(input('Please print a count of seconds to calculate: '))
hour = time // 3600
minute = (time - (hour * 3600)) // 60
second = (time - (hour * 3600) - (minute * 60))
print(f'HOURS/MINUTES/SECONDS: {hour:02}:{minute:02}:{second:02}')
