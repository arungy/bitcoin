
//How do you find the missing number in a given integer array of 1 to 100? (solution)

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void init(int data[], int N)
{
    for (int i = 0; i < N; i++) {
        //rand()%(max-min + 1) + min
        data[i] = rand()%(N - 1 + 1) + 1;
    }
}

void print(int data[], int N)
{
    for (int i = 0; i < N; i++) {
        cout << data[i] << " ";
    }
    cout << endl;
}

void print_small_large(int data[], int N)
{
    int min = 1, max = 1;
    for (int i = 1; i <= N; i++) {
        if (data[i] > 0) {
            min = i < min ? i : min;
            max = i > max ? i : max;
        }
    }
    cout << "small: " << min << " " << "large: " << max;
}

void find_small_large(int out[], int data[], int N)
{
    for (int x = 0; x < N; x++) {
        int t = data[x];
        out[t] += 1;
    }
}

int main()
{
    const int N = 100;
    int array[N];
    int out[N + 1] = {0};
    
    init(array, N);
   
    find_small_large(out, array, N);
    
    sort(array, array + N);
    print(array, N);
    
    print_small_large(out, N + 1);
    
	return 0;
}