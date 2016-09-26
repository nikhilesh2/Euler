#find the 10001 prime number
import math
def main():
	return findNthPrime

def findFactors(num):
	factors = []
	i = 1
	while i <= math.sqrt(num):
		if (num % i == 0):
			factors.append(i)
			factors.append(num / i)
		i += 1
	
	return factors

def findNthPrime(num):
	currValue = 0
	counter = 0
	ans = 0
	while(counter <= num):
		currValue +=1
		if(len(findFactors(currValue)) == 2):
			counter += 1
			ans = findFactors(currValue)[1]
		
	return ans
print findNthPrime(10001)
