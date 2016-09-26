#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import math
a = 1
b = 1
c = 1
for a in range(1,1000):
	for b in range(1,1000-a):
		c = 1000 - a - b
		if(a ** 2 + b ** 2 == c ** 2):
			print a*b*c
