#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams
import copy

commodity_of_bear = []

salary = int(input("please input your salary:"))

commodity = [[1, "iPhone", 5800], [2, "bike", 800], [3, "book", 600], [4, "desk", 100], [5, "gift", 900]]

for i in range(5):
    if (commodity[i][2] <= salary):
        commodity_of_bear.append(commodity[i])
    else:
        continue

length_bear = len(commodity_of_bear)
print("The commodity you can bear are:")
for i in range(length_bear):
    print("number of commodity is " + str(commodity_of_bear[i][0]) + ','
          + "the name of commodity is " + commodity_of_bear[i][1] + ','
          + "the price of commodity is " + str(commodity_of_bear[i][2]))

n_number = int(input("How many commoditys do you want to buy ?"))


def buy():
    n_recycle = 1
    count = 0
    while (n_recycle <= n_number):
        number_of_commodity = int(input("please input the number of commodity you want:"))
        for gg in range(length_bear):
            if number_of_commodity == commodity_of_bear[gg][0]:
                count += commodity_of_bear[gg][2]
            else:
                continue
        n_recycle += 1
    return count


count = buy()
while True:
    print("You need to pay for commodity:" + str(count))
    if (count <= salary):
        print("your salary decrease:" + str(salary - count))

    else:
        print("Do you want to chose again:")
        chose = input("T/N?")
        if (chose == 'Y'):
            print("please chose again:")
            count = buy()
        else:
            break
