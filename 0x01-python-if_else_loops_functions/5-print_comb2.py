#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{num:02d},".format(num=i), end=" ")
