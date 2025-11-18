month_list =["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
#total = 0

total = int(input("Enter number of months it rained ")) #User enters in how many months that it rained

for n in range(1,total):
     print(month_list[n])
     amount = int(input("Enter rainfall ")) #User enters in mow much rainfall per month
     sum = total + amount
     total += sum(amount)

print("Total amount of rainfall was", sum(total))

average = amount / total

print("The average is",average)