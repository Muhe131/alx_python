def fibonacci_sequence(n):
     p  = 0
     q = 1
     n = int (input ("Enter the number of terms: "))
     i = 2
     list = [p, q]
     while i<n:
          fibo = p+q
          list.append(fibo)
          p = q
          q = fibo
          i+=1
          print(list , end=" ")