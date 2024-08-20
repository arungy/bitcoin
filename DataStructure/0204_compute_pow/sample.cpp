
#include <iostream>
using namespace std;

int calc_pow(int x, int n)
{
    int pow = 1;
    for (int i = 0; i < n; i++) {
        pow *= x;
    }
    
    return pow;
}

//optimized version
int calc_pow2(int x, int n)
{
    if (n == 0)
        return 1;
    
    int tmp = calc_pow2(x, n / 2);
    tmp = tmp * tmp;
    
    if (n % 2 == 0) {
        return tmp;
    } else {
        return tmp * x;
    }
}

void compute_power(int x, int n)
{
    cout << "Compure power of " << x << " and " << n << " is : " << calc_pow2(x, n) << endl;
}

int main()
{
    compute_power(9, 25);
        
    return 0;
}
