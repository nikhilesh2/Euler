import math
def main():
	sum = 2 
	x = 3
	while x < 2000000:
		if(isPrime(x) == True):
			sum += x
		x += 1
	
	return sum

def isPrime(num):
	counter = 2
	while counter <= math.sqrt(num):
		if(num % counter == 0):
			return False
		counter += 1
	return True




