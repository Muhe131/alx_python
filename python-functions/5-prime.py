from math import sqrt
def is_prime(number):
     if number<=1 or (number % 2 == 0 and number >2):
          return False
     return all (number % i for i in range(3, int(sqrt(number)) + 1, 2))