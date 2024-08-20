
#include <iostream>
using namespace std;

//more optimized version
int CountBits(int x)
{
    int cnt = 0;
    while (x > 0) {
        if ( x & 1)
            cnt += 1;
        x = x >> 1;
    }

    return cnt;
}

int table[256];
//more optimized version
int CountBits3(int x)
{
    table[0] = 0;
    
    for (int i = 1; i < 256; i++) {
        table[i] = (i & 1) + table[i / 2];
    }
    
    //for (int i = 0; i < 256; i++) {
    //    cout << i << " -> " << table[i] << endl;
    //}
    
    int cnt = table[x & 0xff];
    x >>= 8;
    
    cnt += table[x & 0xff];
    x >>= 8;
    
    cnt += table[x & 0xff];
    x >>= 8;
    
    cnt += table[x & 0xff];
    x >>= 8;

    return cnt;
}


void bit_set(int x)
{
    cout << "Number of bit set for " << x << " is: " << CountBits3(x) << endl;
}

int main()
{
    bit_set(32767);
    bit_set(15);
        
    return 0;
}
