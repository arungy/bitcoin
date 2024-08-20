
#include <iostream>
#include <cstring>

using namespace std;

int binary_search(int data[], int find, int l, int h)
{
    if (l >= h) {
        return (find > data[l] ? l + 1 : l);
    }

    int mid = (h + l) / 2;

    if (find == data[mid]) {
        return mid + 1;
    }

    if (find > data[mid]) {
        return binary_search(data, find, mid + 1, h);
    }

    return binary_search(data, find, l, mid - 1);
}

void print(int elem[], int n)
{
    for (int i = 0; i < n; i++) {
        printf("%d ",elem[i]);
    }
    printf("\n");
}

void sort(int data[], int n)
{
    int j, find, loc;
    for (int i = 1; i < n; ++i) {
        print(data, n);

        j = i - 1;
        find = data[i];

        loc = binary_search(data, find, 0, j);

        while(j >= loc) {
            data[j + 1] = data[j];
            j--;
        }
        data[j + 1] = find;
    }

    print(data, n);
}


int main()
{
    int a[] = {37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54};

    int sz = sizeof(a) / sizeof(a[0]);

    sort(a, sz);

    return 0;
}