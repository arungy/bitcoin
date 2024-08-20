#include <stdio.h>

void print_data(int elem[], int n)
{
    for (int x = 0; x < n; x++) {
        printf("%d ", elem[x]);
    }
    printf("\n");
}

int partition(int data[], int lw, int hi)
{
    int elem = data[hi];
    
    int id = lw;
    
    for (int e = lw; e < hi; e++) {
        if (elem >= data[e]) {
            int tmp = data[id];
            data[id] = data[e];
            data[e] = tmp;
            
            id += 1;
        }
    }
    
    int tmp = data[id];
    data[id] = data[hi];
    data[hi] = tmp;
    
    return id;
}

void quick_sort(int data[], int low, int high)
{
    if (low < high) {
        
        int pi = partition(data, low, high);
        
        quick_sort(data, low, pi - 1);
        
        quick_sort(data, pi + 1, high);
    }
}

int main() 
{
    int data[] = {1, 4, -5, 6, 89, 50, 24};
    int sz = sizeof(data) / sizeof(data[0]);
    
    print_data(data, sz);
    
    quick_sort(data, 0, sz - 1);

    print_data(data, sz);
}