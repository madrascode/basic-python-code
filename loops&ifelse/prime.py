def prime(num):
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				print(str(num)+" is not Prime number")
				print(str(i)+" times "+str(num//i)+" is "+str(num))
				break
		else:
			print(str(num)+" is Prime number")
			
	else:
		print("number is less than 1 it cannot be prime.")


prime(6)
