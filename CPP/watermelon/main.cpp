//
//watermelon: https://codeforces.com/problemset/problem/4/A
//

#include <iostream>
using namespace std;

int divide_watermelon(int w)
{
    int even = 0;
    for(int i = 2; i < w; i += 2) {
        int rem = w % i;
        if ((rem % 2) == 0) {
            even = 1;
        } else {
            even = 0;
            break;
        }
    }
    
    return even;
}

int main()
{
    int weight = 0;
    
    cout << "Enter the weight: ";
    cin >> weight;
    
    int ret = divide_watermelon(weight); 
    cout << (ret ? "YES" : "NO");
    
    return 0;
}