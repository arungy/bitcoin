
#include <iostream>
using namespace std;

void recursive_1_to_n(int x)
{
    if (x <= 0)
        return;
    
    cout << x << endl;
    recursive_1_to_n(x - 1);
}

int main()
{
    recursive_1_to_n(10);
        
    return 0;
}
