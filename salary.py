days = int(input('Enter the number of days: '))

def salary():
  day = 0
  pennie = 1
  while days > day:
    day = day + 1
    print('Day number: ',day, 'Salary in pennies: ',pennie, 'salary in dollars: $',(pennie / 30))
    pennie = pennie * 2
    print('total pay earned: $',format(pennie,'.2f'))

salary()
