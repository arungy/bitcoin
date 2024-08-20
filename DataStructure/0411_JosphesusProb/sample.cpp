
#include <iostream>
#include <string>
using namespace std;

void JosProb(int n, int k)
{
    if (N == 1) {
        cout << "Move 1 from " << a << " to " << c << endl;
        return;
    }
    
    
    HonaiTower(N - 1, a, c, b);
    cout << "Move " << N << " from " << a << " to " << c << endl;
    HonaiTower(N - 1, b, a, c);
}

int main()
{
    JosProb(4, 2);
        
    return 0;
}
