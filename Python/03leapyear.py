
import sys

def main():
    print('Enter the year')
    
    yr = int(input())
    
    if ((yr % 4) == 0 and (yr % 100) != 0) or ((yr % 400) == 0):
        print('LEAP')
    else:
        print('COMMON')

if __name__ == '__main__':
    main()
    sys.exit(0)
    