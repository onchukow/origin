day1 = float(input('First day distance (km): '))
goal = float(input('Goal distance (km): '))
days = 1
while day1 < goal:
    day1 = day1 * 1.1
    days +=1
print(f"Goal will be reached on the {days}'s day")