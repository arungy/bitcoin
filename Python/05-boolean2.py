
A = 0
print("The Boolean value for trivial integer is", bool(A))

B = 1
print("The Boolean value for non-trivial integer is", bool(B))

f1 = 0.0
print("The bool of trivial value of float is", bool(f1))

f2 = 0.001
print("The bool of non-trivial value of float is", bool(f2))

print("\n" + "-"*7 + "Bool of String" + "-"*7)
s1 = ""
print("The bool of trivial value of string is", bool(s1))

s2 = " " # a string with a space is a non-trivial string
print("The bool of non-trivial value of string is", bool(s2))

s3 = "Apple"
print("The bool of non-trivial value of string is", bool(s3))

a = range(5)
print(a)

print(range(2, 9))

print(range(2, 9, 3))
print(range(3, -3, -2))