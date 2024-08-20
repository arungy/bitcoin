
#include <iostream>
using namespace std;

void IsTwoOddOccur(int data[], int size)
{
    int max = data[0], res = 0;
    for (int i = 0; i < size; i++){
        res = res ^ data[i];
        //max = data[i] > max ? data[i] : max;
    }
    
    cout << res;
}

void IsTwoOddOccur2(int data[], int size)
{
    int xorval = 0, res1 = 0, res2 = 0;
    for (int i = 0; i < size; i++){
        xorval = xorval ^ data[i];
    }
    //cout << xorval;
    
    int sb = xorval & ~(xorval - 1);
    for (int i = 0; i < size; i++){
        if (data[i] & sb) {
            res1 = res1 ^ data[i];
        } else {
            res2 = res2 ^ data[i];
        }
    }
    
    cout << res1 << " " << res2;
}

void odd_occuring(int data[], int size)
{
    IsTwoOddOccur2(data, size);
}

int main()
{
    //int arr[] = {3, 4, 3, 4, 5, 4, 4, 6, 7, 7};
    int arr[] = {17, 20, 20};
    
    odd_occuring(arr, (sizeof(arr)/ sizeof(arr[0])));
        
    return 0;
}
