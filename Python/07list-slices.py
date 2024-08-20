
import sys

def main():
    A = [1, 2, 3, 4, 5, 6, 7]
    A[::-2] = [10, 20, 30, 40]
    print(A)
    
if __name__ == '__main__':
    main()
    sys.exit(0)
