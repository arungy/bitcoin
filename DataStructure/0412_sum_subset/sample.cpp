
#include <iostream>
#include <string>
using namespace std;

void subset(int set[], int k, int n, int len)
{
    if (n == len) {
        int t = k;
        while (t < n) {
            cout << set[t++] << " ";
        }
        cout << endl;
        return;
    }
    
    
    subset(set, k,     n + 1, len);
    subset(set, k + 1, n + 1, len);
}

int main()
{
    int data[] = {2, 3, 4};
    subset(data, 3);
        
    return 0;
}
