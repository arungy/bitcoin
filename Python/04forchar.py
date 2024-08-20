
import sys

def main():
    for ch in 'Hello':
        print(ch)
    print()
    
    for i in range(3, 8):
        print(i, i**2)
    print('end of loop\n')
    
    for i in range(8):
        print(i)
    print()
    
    for i in range(2 ** 2):
        print('Hello, world!')
    print()
    
    for i in range(-5):
        print('Hello, world!')
    print()
    
    res = 0
    num = 5
    for i in range(1, num + 1):
        res += i
    print('sum of integer from 0 to', num, 'is', res)
    print()
    
    for i in range(10, 0, -2):
        print('i:', i)
    print()
    
    print(1, 2, 3)
    print(4, 5, 6)
    print(1, 2, 3, sep=', ', end='. ')
    print(4, 5, 6, sep=', ', end='. ')
    print()
    print(1, 2, 3, sep='', end=' -- ')
    print(4, 5, 6, sep=' * ', end='.')
    

if __name__ == '__main__':
    main()
    sys.exit(0)
    