
count = 0
i = 1
while(True):
	for x in range(1,20):
		if(i % x == 0):
			count += 1

	if(count >= 20):
		count = 0
		print i
		break
	
	count = 0
	i += 1
