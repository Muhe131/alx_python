#!/usr/bin/python3
def reverse_string(string):
     reverse  =  ' ' #declaring empty string to store the reversed string
     for i in range ( len(string),  0, -1):
          reverse += string[i  - 1]
          return reverse
