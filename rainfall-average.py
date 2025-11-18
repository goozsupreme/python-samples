month_list =["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
store = []
total = 0

total = int(input("Enter number of months it rained ")) #User enters in how many months that it rained

for n in range(0,total):
     print(month_list[n])
     amount = int(input("Enter rainfall ")) #User enters in mow much rainfall per month
     store.append(amount)

total_sum = sum(store)
print(f"Total amount of rainfall was {total_sum}")

average = total_sum / len(store)
print(f"The average amount of rainfall was {average}")