
x = 4
y = 5
print(x is y)  # 'is'
print("ID of x is:", id(x))
print("ID of y is:", id(y))

a = 7
b = 8
print(a is not b) # 'is not'
print("ID of a is:", id(a))
print("ID of b is:", id(b))

s = "Apple"
t = s
print(s is not t)
print("Id of s is:", id(s))
print("Id of t is:", id(t))