#!/usr/bin/python

import random
import math

def multiply(z,y):
	sum = 0
	for x in range(y):
		sum = sum + z
	return sum

def divide(x,y):
	if y==0:
		return "divison by zero"
	count = 0
	# x = int(x)
	# y = int(y)
	while (((x-y) >= 0) ):
		print x-y
		x = (x-y)
		count = count + 1
	return count

	# for z in range(y):
	# 	while 


if __name__ == '__main__':
	# print (multiply(9,9))
	print (divide(8,4))
