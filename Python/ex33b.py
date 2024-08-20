def append_numbers(numbers, nCount):
	i = 0
	while i < nCount:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	

print "The numbers: "

maxNum = 10
TotNum = []

append_numbers(TotNum, maxNum)


for num in TotNum:
	print num


