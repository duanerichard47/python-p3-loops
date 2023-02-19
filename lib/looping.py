#!/usr/bin/env python3

#def happy_new_year():
  #  for i in range(10, 0, -1):
   #     print(i)
    
    #print("Happy New Year!")
def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i = i - 1
    print("Happy New Year!")
    
#def square_integers(int_list):
  #  return [i ** 2 for i in int_list]

def square_integers(int_list):
    new_list = list()
    for interger in int_list:
        new_list = interger * interger
    return new_list

def square_integers(int_list):
    return [integer * integer for integer in int_list]

#def fizzbuzz():
   # for i in range(1, 101):
    #    if not i % 15:
     #       print("FizzBuzz")
     #   elif not i % 5:
    #        print("Buzz")
    #    elif not i % 3:
     #       print("Fizz")
      #  else:
       #     print(i)

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
