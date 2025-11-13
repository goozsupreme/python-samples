#this doesn't work still testing

import math

my_list =["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
total = 0

total = int(input("Enter number of months it rained ")) #User enters in how many months that it rained

for n in range(0,total):
     print(my_list[n])
     amount = int(input("Enter rainfall ")) #User enters in mow much rainfall
     total += amount #Concatenate the total months they entered and the total amount of rainfall they entered

print("Total is",total) #Prints total amount of months or rainfall?

print(min(amount))
print(max(amount))

average = total (amount)
print("The average is",average)