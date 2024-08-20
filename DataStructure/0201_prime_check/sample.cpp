
#include <iostream>
using namespace std;

int IsPrime(int x)
{
    if (x <= 0 || x == 1) {
        return false;
    }
    
    for (int n = 2; n < x; n++) {
         if((x % n) == 0) {
          return false;
        }
    }
    
    return true;
}

//optimized version
int IsPrimeOpt(int x)
{
    if (x <= 0 || x == 1) {
        return false;
    }
    
    for (int n = 2; (n * n) <= x; n++) {
         if((x % n) == 0) {
          return false;
        }
    }
    
    return true;
}

//more optimized version
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

void check_prime(int num)
{
    cout << num <<" is " << (true == IsPrimeOpt2(num) ? "prime" : "not prime") << " number." << endl;
}

int main()
{
    check_prime(37);
    check_prime(1);
    check_prime(100);
    check_prime(1031);
        
    return 0;
}