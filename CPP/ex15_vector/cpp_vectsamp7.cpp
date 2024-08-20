
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
    vector<bool> b {true, false, true, false, true, true, false, true};
    
    // auto cannot be used for bool
    //for (auto &bval : b) {
    //    cout << bval << " ";
    //}
    
    for (size_t i = 0; i < b.size(); i++) {
        cout << b[i] << " ";
    }
    cout << "\n";
    
    cout << *b.begin() << "\n";
    cout << "bool size: " << b.size() << "\n";
    
    return 0;
}
