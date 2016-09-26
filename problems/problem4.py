def main():
	max = 0
	for x in range(999):
		for y in range(999):
			product = x * y	
			if(checkPal(product) == True and product > max):
				max = product
	return max

def checkPal(num):
	return str(num) == str(num)[::-1]
		

