
#include <iostream>
using namespace std;

void IsOneOddOccur(int data[], int size)
{
    for (int i = 0; i < size; i++){
        for (int j = i + 1; j < size; j++){
            if (data[i] > 0 && data[i] == data[j]) {
                data[i] = data[j] = 0;
                break;
            }
        }
    }
    
    for (int i = 0; i < size; i++){
        if (data[i]) {
            cout << data[i] << " ";
        }
    }
}

void IsOneOddOccur2(int data[], int size)
{
    int res = 0;
    for (int i = 0; i < size; i++){
        res = res ^ data[i];
    }
    
    cout << res;
}

void IsOneOddOccurVariation(int data[], int size)
{
    int res = 0, res1 = 0;
    
    int min = data[0], max = data[0];
    for (int i = 1; i < size; i++){
        res = res ^ data[i];
        min = data[i] < min ? data[i] : min;
        max = data[i] > max ? data[i] : max;
    }
    
    for (int i = min; i <= max; i++){
        res1 = res1 ^ i;
    }
   
    cout << (res ^ res1);
}

void odd_occuring(int data[], int size)
{
    IsOneOddOccurVariation(data, size);
}

int main()
{
    //int arr[] = {4, 3, 4, 4, 4, 5, 5};
    //int arr[] = {8, 7, 7, 8, 8};
    int arr[] = {7, 9, 10, 11};
    
    odd_occuring(arr, (sizeof(arr)/ sizeof(arr[0])));
        
    return 0;
}
