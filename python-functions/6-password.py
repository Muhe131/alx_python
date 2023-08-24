def validate_password(password):

          upper = False
          lower = False
          digit = False

          if " " in password:
               return False
          if len(password) < 8:
               return False
          for i in password:
               if(i. isupper()):
                    upper = True
               elif (i.islower()):
                    lower = True
               elif (i.isdigit):
                    digit = True
          if upper and lower and digit:
               return True
          else:
               return False