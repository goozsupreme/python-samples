has_uppercase = True
has_lowercase = True
has_digit = True

password = input("Enter password ")

for char in (password):
     if not (len(password) > 8):
          print("passowrd is too short")
          break

     if (password.isupper()):
          has_uppercase = False
          print("Missing uppercase")
          break

     if (password.islower()):           #has_lowercase is not working
          has_lowercase = False
          print("Missing lowercase")
          break
     
     if (password.isdigit()):           #has_digit is not working
          has_digit = False
          print("Missing digit")
          break

     else:
          print("Good password")
          break