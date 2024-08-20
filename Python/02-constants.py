
PI = 3.1415
print(PI)

radius = 5.0
c = 2 * PI * radius
print('The circumference of a circle of a radius %0.2f is: %0.2f' %(radius, c))

b = 10
print(b, type(b))

b = 10.1
print(b, type(b))

a = 5
b = float(a)
c = int(b + 2)
print("data type conversion =>", a, b, c)

print('-'*5 + "Convert string to int & float" + '-'*5 )
A = '14'
B = int(A) #int(A), we are typcasting A to an integer
C = float(A) #float(A), we are typcasting A to an floating point
print(B, C)