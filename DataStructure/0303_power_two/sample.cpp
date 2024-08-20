
#include <iostream>
using namespace std;

//more optimized version
int IsPowerTwo(int x)
{
    int cnt = 0;
    while (x > 0) {
        x = x & (x - 1);
        cnt += 1;
    }
    
    return (1 == cnt ? true : false);
}

//more optimized version
int IsPowerTwo2(int x)
{
    return ((x != 0) && (x & (x - 1) == 0));
}

void power_two(int x)
{
    cout << x << " is power of 2" << ": " << (true == IsPowerTwo(x) ? "Yes" : "No") << endl;
}

int main()
{
    power_two(32767);
    power_two(16);
    power_two(256-1);
        
    return 0;
}
