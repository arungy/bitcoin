
#include <iostream>
using namespace std;

//more optimized version
int IsKthBitSet(int x, int n)
{
    if ( x & (1 << n - 1))
        return true;
    
    return false;
}


void bit_set(int x, int n)
{
    cout << "for " << x << ", bit " << n <<" is set: " << (true == IsKthBitSet(x, n) ? "yes" : "no") << endl;
}

int main()
{
    bit_set(1, 1);
    bit_set(7, 2);
        
    return 0;
}
