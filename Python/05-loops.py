
arange = range(5)

for i in arange:
	print(i)

print("\n" + '-'*8)
b = range(1, 7)
for i in b:
	if i % 5 == 0:
		print(i)
		break
	else:
		print(i, "is not 5!")

print("\n" + '-'*8)
vrange = range(22, 30)
for v in vrange:
	if v % 6 == 0:
		continue
	print(v, "is not multiple of 6")

for i in range(3):
	pass