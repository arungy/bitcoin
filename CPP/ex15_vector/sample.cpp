
#include <iostream>
#include <vector>
#include <list>
#include<bits/stdc++.h>

using namespace std;

void print (vector<int> vi)
{
    for(const auto &v : vi) {
        cout << v << " ";
    }
    cout << endl;
}

int main()
{
    vector<int> vi {1, 5, 10, 15};

    print(vi);

    vi.push_back(30);
    print(vi);

    remove_copy(vi.begin(), vi.end(), vi.begin(), 40);
    print(vi);

    vi.pop_back();
    print(vi);
    
    int *p = vi.data();
    for (int i = 0; i < vi.size(); i++) {
        cout << p[i] << " ";
    }
    cout << endl;

    return 0;
}
