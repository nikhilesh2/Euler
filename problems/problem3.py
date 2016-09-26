#What is the largest prime factor of the number 600851475143 ?
import math

def main():
	maxPrime = 0
	maxPrimeArr = []
	arr = findPrime(600851475143)		

	for x in range(len(arr)):
		if(len(findPrime(arr[x])) == 2 and arr[x] > maxPrime):
			maxPrime = arr[x]

	
	return maxPrime



def findPrime(num):
	factors = []
	i = 1
	while i <= math.sqrt(num):
		if (num % i == 0):
			factors.append(i)
			factors.append(num / i)
		i += 1
	
	return factors

