#By considering the terms in the Fibonacci sequence whose values do not exceed 
#four million, find the sum of the even-valued terms.
def main():
	previousNum1 = 1
	previousNum2 = 1
	currentNum = 0
	evenNumSum = 0

	while(currentNum < 4000000):
		if(currentNum % 2 == 0):
			evenNumSum += currentNum		
		currentNum  = (previousNum1 + previousNum2)
		previousNum1 = previousNum2
		previousNum2 = currentNum

	return evenNumSum



	