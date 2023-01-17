#!/usr/bin/python3

for firstnumber in range(0, 10):
    for secondnumber in range(0, 10):
        if (firstnumber != secondnumber and firstnumber < secondnumber):
            print(str(firstnumber) + str(secondnumber), end=", ")
