def validate_password(password):
     val = True
     if len(password) < 8:
          print('length should be at least  8')
          val = False
          if password.count( " ") > 0 :
               print('error , one or more spaces in password')
               val = False
     #Check if password contains at least one digit, uppercase letter, lowercase letter, and Special symbols
     has_digit = True
     has_upper = True
     has_lower = True
     for char in password :
          if ord(char) >= 48 and ord(char) <= 57:
               has_digit = True
          elif ord(char) >= 65 and ord(char) <= 90:
               has_upper = True
          elif ord(char) >= 97 and ord(char) <= 122:
               has_lower = True
     if not has_digit:
          print('password should have at least one numeral')
          val = False
     if not has_upper:
          print('password should have at least one uppercase letter')
          val = False
     if not has_lower:
          print('password should have at least one lowercase letter')
          val = False
          return val