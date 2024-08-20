
#include <iostream>
using namespace std;

int IsPrimeOpt2(int x)
{
    if (x <= 0 || x == 1) {
        return false;
    }
    
    if (x == 2 || x == 3) {
        return true;
    }
    
    if ((x % 2) == 0 || (x % 3) == 0) {
        return false;
    }
    
    for (int n = 5; (n * n) <= x; n += 6) {
         if((x % n) == 0 || (x % (n + 2)) == 0) {
          return false;
        }
    }
    
    return true;
}

void IsPrimeFactor(int x)
{
    for (int n = 2; n <= x; n += 1) {
        if (IsPrimeOpt2(n)) {
            int t = n;
            while ((x % t) == 0) {
                cout << n << " ";
                t *= t;
            }
        }
    }
}

void IsPrimeFactor2(int x)
{
    if (x <= 1) { return; }

    for (int n = 2; n * n <= x; n += 1) {
        while ((x % n) == 0) {
            cout << n << " ";
            x /= n;
        }
    }
    
    if (x > 1)
        cout << x << " ";
}

//more optimized
void IsPrimeFactor3(int x)
{
    if (x <= 1) { return; }
    
    while (x % 2 == 0) {
        cout << 2 << " ";
        x /= 2;
    }
    
    while (x % 3 == 0) {
        cout << 3 << " ";
        x /= 3;
    }
    
    if (x % 2 == 0 || x % 3 == 0) {
        return;
    }

    for (int n = 5; n * n <= x; n += 6) {
        while (x % n == 0) {
            cout << n << " ";
            x /= n;
        }
        
        while (x % (n + 2) == 0) {
            cout << n + 2 << " ";
            x /= (n + 2);
        }
    }
    
    if (x > 2)
        cout << x << " ";
}

void check_primefactor(int num)
{
    cout << "Prime factor for " << num << " is : ";
    IsPrimeFactor3(num);
    cout << endl;
}

int main()
{
    check_primefactor(12);
    check_primefactor(121);
    check_primefactor(450);
    check_primefactor(1031);
        
    return 0;
}