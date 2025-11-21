days = int(input('Enter the number of days: '))

def salary():
  day = 0
  pennie = 1
  while days > day:
    day = day + 1
    print('Day number: ',day, ' Salary in pennies:',pennie, ' Salary in dollars: $',format(pennie / 2,'.2f'))
    pennie = pennie * 2
    print('Total pay earned: $',format(pennie,'.2f'))

salary()
