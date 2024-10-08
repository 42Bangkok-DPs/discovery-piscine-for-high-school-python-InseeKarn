#!/usr/bin/env python3
import numpy
table1 = [2, 8, 9, 48, 8, 22, -12, 2]
table2 = numpy.array(table1)

print("Original array: ", table1)
print ("New array: " + "[" + ", ".join(map(str, table2 * 2)) + "]")