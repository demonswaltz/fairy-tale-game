count = 0
x= 10
y = 0

def lessthanfive():
	while count < 5:
		print count, " is  less than 5"
		if x < 50:
			count = count + 1
			x-= 1
		elif y < 8:
			count -= 1
			x += 5
		elif x + y < 22:
			count += 1
	else:	
	   print count, " is not less than 5"
	   
lessthanfive()
