
#include <iostream>
#include <string>
using namespace std;

void HonaiTower(int N, char a, char b, char c)
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
    HonaiTower(3, 'A', 'B', 'C');
        
    return 0;
}
