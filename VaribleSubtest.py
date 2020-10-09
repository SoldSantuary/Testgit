from math import *

from os import system, name
from time import sleep
# define our clear function
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')
# print out some text
print('Hi !! I am Python\n'*10)
sleep(2)
# now call function we defined above
screen_clear()


Char_age = 50.575
Char_name = "Erik"
is_Male = True
print()
# new line \n
print("There once was a man \n named " + Char_name + ",")
# use float for numbers with decimals and whole numbers.
print("he was " + (str(Char_age)) + " years old.")
print("He really liked the name " + Char_name + ", ")
print("but didn't like being " + (str(Char_age)) + ".")
print()
joy = (abs(Char_age))
#done with abs function
print((abs(Char_age)) , 'is the absolute number')
#done with variable joy
print (joy, 'is the absolute number')

joy2 = ()

#name = input("Enter your name")
#print("hello " + name + "!")
