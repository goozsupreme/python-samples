#input
#input data and convert to fahrenheit
dbltempurature = float(input("Enter celsius tempurature "))
dblcelsius = dbltempurature
dblfahrenheit = dblcelsius

#process
#convert celsius to fahrenheit
dblfahrenheit = dblcelsius * 1.8 + 32

#output
#fahrenheit tempurature
#celsius tempurature
print ("The fahrenheit tempurature is",format(dblfahrenheit,".2f"))
