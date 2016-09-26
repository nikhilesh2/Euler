#find the difference between  the square of the sum and the sum of the squares of the numbers up to 100
sumOf = 0
squareOf = 0

for x in range(101):
	squareOf += x
	sumOf += x*x

print squareOf*squareOf - sumOf