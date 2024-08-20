
print(bool(0))  #trivial value is false

print(bool(100)) #non-trivial is true

print(bool(0.0))

print(bool(0.123))

print(bool(""))  #empty string is converted to False

print(bool(" ")) #non-empty string is converted to True

print(bool("Zebra")) #non-empty string is converted to True

a = 0
print("a = ", a)
if a:
	print("Non-zero")
else:
	print("Zero")

a = 1
print("a = ", a)
if a:
	print("Non-zero")
else:
	print("Zero")

