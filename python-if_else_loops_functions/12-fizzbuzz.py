#!/usr/bin/python3


def fizzbuzz():
    for fizzbuzz in range (1, 101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 ==0:
            print("FizzBuzz", end=" ")
        elif fizzbuzz % 5 == 0:
            print("Buzz", end=" ")
        elif fizzbuzz % 3 == 0:
            print("fizz", end=" ")
        else:
            print(fizzbuzz, end=" ")


    


