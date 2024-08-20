
#include <iostream>
using namespace std;

//more optimized version
double calc_pow3(double x, int n)
{
    double pow = 1;
    while (n > 0) {
        if (n % 2 != 0) {
            pow *= x;
        } 
        x = x * x;
        n = n / 2;
    }
    
    return pow;
}


void compute_power(int x, int n)
{
    cout << "Compure power of " << x << " and " << n << " is : " << calc_pow3(x, n) << endl;
}

int main()
{
    compute_power(9, 25);
        
    return 0;
}
