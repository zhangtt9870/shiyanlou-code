nums = range(1,101)

for num in nums :
	if num % 7 == 0 or num % 10 == 7 or num // 10 ==7:
		continue
	else:
		print(num, end=' ')
