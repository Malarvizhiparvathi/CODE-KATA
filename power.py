def isPowerOfTwo(num):
	if (num == 0):
		return False
	while (num != 1):
			if (num % 2 != 0):
				return False
			num = num // 2
	return True
num=int(input(""))
if(isPowerOfTwo(num)):
    print("yes")
else:
    print("no")
