
#include <iostream>
#include <vector>
#include <list>

#include <algorithm>
using namespace std;

void fun(const int& value) {
    cout << value << " ";
}

int main()
{
    vector<int> v {100, 101, 102, 103, 104, 105, 106, 107};
    
    for (auto it = begin(v); it != end(v); it++) {
        cout << *it << " ";
    }
    cout << "\n";
    
    for_each (begin(v), end(v), fun);
    cout << "\n";
    
    //lambda functions
    cout << "lambda: ";
    for_each (begin(v), end(v), [](auto &value) {
        cout << value << " ";
    });
    cout << "\n";
    
    for (vector<int>::iterator it = begin(v); it != end(v); it++) {
        cout << *it << " ";
    }
    cout << "\n";
    
    for (size_t i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << "\n";
    
    return 0;
}
