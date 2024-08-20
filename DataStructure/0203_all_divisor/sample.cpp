
#include <iostream>
using namespace std;

int IsDivisor(int x)
{
    for (int n = 1; n * n <= x; n += 1) {
         if (x % n == 0) {
          cout << n << " ";
          if (n != x / n) {
            cout << x / n << " ";
          }
        }
    }
    
    return 0;
}

//more optimized
int IsDivisor2(int x)
{
    int n;
    for (n = 1; n * n < x; n += 1) {
         if (x % n == 0) {
          cout << n << " ";
        }
    }
    
    for (; n >= 1; n -= 1) {
         if (x % n == 0) {
          cout << x / n << " ";
        }
    }
    
    return 0;
}

void check_alldivisor(int num)
{
    cout << "All divisor for " << num << " is : ";
    IsDivisor2(num);
    cout << endl;
}

int main()
{
    check_alldivisor(100);
    check_alldivisor(7);
    check_alldivisor(450);
        
    return 0;
}
