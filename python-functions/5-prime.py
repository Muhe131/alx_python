from math import sqrt
def is_prime(number):
     if number<=1 or (number % 2 == 0 and number >2):
          return False
     return all (number % i for i in range(3, int(sqrt(number)) + 1, 2))
    #else:
          #for x in range(2,number):
            #   if(number % x==0):
            #        return False
         #      return True
          #print(is_prime(9))