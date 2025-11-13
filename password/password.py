# this doesnt work, still testing

upper = 0
lower = 0
digit = 0

password = input("Enter password ")

for x in password:
     for i in range(len(password)>=8):
          if(password.isupper()):
                    upper = 1
          elif(password.islower()):
                    lower = 1
          elif(password.isdigit()):
                    digit = 1
          else:
               print("Please try again")
