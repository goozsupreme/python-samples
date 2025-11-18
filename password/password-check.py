# this doesnt work, still testing

upper = bool
lower = bool
digit = bool
value = bool

password = input("Enter password ")

def password_check(password):
    if len(password) <=6:
        print("bad password")
        value = True
        
    elif(password.isupper()):
        print("bad password")
        upper = True
        
    else:
        print("good password")