TAXRATE = 0.08

def printme():
     print("header")

def tax():
     print(" ")
     print("TAX")
     dblamount = float(input("Enter amount: "))
     dbltotal = dblamount * TAXRATE
     dblr = dbltotal + dblamount
     print("Tax:",dbltotal)
     print("Total tax",dblr)

def add2():
     print(" ")
     print("ADD 2")
     dblnumber1 = float(input("Enter number: "))
     dblnumber2 = float(input("Enter number: "))
     dbladd = dblnumber1 + dblnumber2
     print(dbladd)

def sqr1():
     print(" ")
     print("SQR1")
     dblnum1 = float(input("Enter number: "))
     dblnum2 = float(input("Enter number: "))
     dblsqr = dblnum1 * dblnum2
     print(dblsqr)

def payday():
     print(" ")
     x = float(input("Enter pay "))
     d = x + 10
     print(d)
  
tax()
add2()
sqr1()
payday()
