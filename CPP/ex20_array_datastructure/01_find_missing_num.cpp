
//How do you find the missing number in a given integer array of 1 to 100? (solution)

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void init(int data[], int N)
{
    for (int i = 0; i < N; i++) {
        data[i] = rand()%101;
    }
    
    //data[11] = data[35] = 10;
}

void print(int data[], int N)
{
    for (int i = 0; i < N; i++) {
        cout << data[i] << " ";
    }
    cout << endl;
}

void print_missnumber(int data[], int N)
{
    for (int i = 0; i < N; i++) {
        if (data[i] == 0) {
            cout << i << " ";
        }
    }
    cout << endl;
}

void find_missnumber(int out[], int data[], int N)
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
    int missnum[N] = {0};
    
    init(array, N);
   
    find_missnumber(missnum, array, N);
    
    sort(array, array + N);
    print(array, N);
    
    print_missnumber(missnum, N);
    
	return 0;
}