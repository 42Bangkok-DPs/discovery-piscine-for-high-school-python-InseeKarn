#!/usr/bin/env python3

import numpy
table1 = [2, 8, 9, 48, 8, 22, -12, 2]
table2 = []
print("Original array: ", table1)

for num in table1:
    newnum = num
    newnum += 2
    if newnum >= 5:
        table2.append(newnum)

print(set(table2))