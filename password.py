has_uppercase = False
has_lowercase = False
has_digit = False
too_short = False

def password_check(password):
     for char in (password):
          if (len(password) < 8):
               too_short = True
               print("password is too short")
               return True
               
          elif (password.isupper()):
               has_uppercase = True
               print("Missing lowercase")
               return True
               
          elif (password.islower()):
               has_lowercase = True
               print("Missing uppercase")
               return True
          
          elif (char.isdigit()):
               has_digit = True
               print("Missing digit")
               return True
          
          else:
               print("Good password")
               break

password_check(password = input("Enter password "))