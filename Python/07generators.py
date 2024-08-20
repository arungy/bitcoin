
import sys

def main():
    print('Inside main')
    
    n = 5
    #a = [0] * n
    #print(a)
    #
    #print('')
    #a = [0 for i in range(5)]
    #print(a)
    
    ans = [i ** 2 for i in range(1, n+1)]
    print(ans)
    
    from random import randrange
    n = 10
    
    randval = [randrange(1,10) for i in range(n)]
    print(randval)
    
    #a = [input() for i in range(int(input()))]
    #print(a)
    



if __name__ == '__main__':
    main()
    sys.exit(0)