
//How do you find the missing number in a given integer array of 1 to 100? (solution)

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void init(int data[], int N)
{
    for (int i = 0; i < N; i++) {
        data[i] = rand() % (100000 - 1 + 1) + 1;
    }
}

void print(int data[], int N)
{
    for (int i = 0; i < N; i++) {
        cout << data[i] << "(" << i << ") ";
    }
    cout << endl;
}

void find_allparis(int data[], int N, int given_num)
{
    for (int x = 0; x < N; x++) {
        int t = data[x];
        for (int y = 0; y < N; y++) {
            if (given_num == (data[y] + t)) {
                cout << x << "," << y << endl;
            }
        }
    }
}

int main()
{
    const int N = 100;
    int array[N];
    
    init(array, N);
    print(array, N);
    find_allparis(array, N, (array[50] + array[20]));
       
	return 0;
}