#!/usr/bin/python3

for firstnumber in range(0, 8):
    for secondnumber in range(1, 10):
        if (firstnumber != secondnumber and firstnumber < secondnumber):
            print("{}".format(firstnumber) + "{}".format(secondnumber), end=", ")
print(89)


