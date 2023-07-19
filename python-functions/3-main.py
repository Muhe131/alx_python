#!/usr/bin/python3
reverse_string = __import__('3-string').reverse_string
string = input( 'Enter the string: ' )
reverse = reverse_string(string)
print("The original string is:", string)
print('The reversed string is:' , reverse)